import os
import warnings
import logging
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chains import RetrievalQA

# Setup
warnings.filterwarnings("ignore")
logging.getLogger("transformers").setLevel(logging.ERROR)
st.title('LeetCode Solution Bot')

# Initialize chat history
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    st.chat_message(message['role']).markdown(message['content'])

@st.cache_resource
def get_vectorstore():
    try:
        pdf_name = "./Leetcode.pdf"  # Make sure this is your PDF file
        loaders = [PyPDFLoader(pdf_name)]
        index = VectorstoreIndexCreator(
            embedding=HuggingFaceEmbeddings(model_name='all-MiniLM-L12-v2'),
            text_splitter=RecursiveCharacterTextSplitter(
                chunk_size=1000, 
                chunk_overlap=200
            )
        ).from_loaders(loaders)
        return index.vectorstore
    except Exception as e:
        st.error(f"Error loading document: {str(e)}")
        return None

# Main chat interface
prompt = st.chat_input('Ask about a LeetCode problem...')

if prompt:
    # Display user message
    st.chat_message('user').markdown(prompt)
    st.session_state.messages.append({'role': 'user', 'content': prompt})
    
    try:
        # Initialize vector store
        vectorstore = get_vectorstore()
        if vectorstore is None:
            st.error("Failed to load the LeetCode solutions document.")
            st.stop()
            
        # Initialize LLM
        groq_chat = ChatGroq(
            groq_api_key=os.environ.get("GROQ_API_KEY"),
            model_name="llama3-8b-8192",
            temperature=0.1  # Lower temperature for more focused answers
        )

        # Create a strict prompt template
        qa_prompt = ChatPromptTemplate.from_template("""
        You are a LeetCode solution assistant. Answer ONLY based on the provided context.
        If the answer is not in the context, say "I couldn't find this in my LeetCode solutions."
        
        Context: {context}
        
        Question: {question}
        
        Answer:
        """)

        # Create the QA chain
        chain = RetrievalQA.from_chain_type(
            llm=groq_chat,
            chain_type='stuff',
            retriever=vectorstore.as_retriever(search_kwargs={'k': 3}),
            chain_type_kwargs={"prompt": qa_prompt},
            return_source_documents=True
        )

        # Get response
        result = chain({"query": prompt})
        response = result["result"]

        # Display response
        st.chat_message('assistant').markdown(response)
        st.session_state.messages.append(
            {'role': 'assistant', 'content': response}
        )

    except Exception as e:
        st.error(f"Error: {str(e)}")