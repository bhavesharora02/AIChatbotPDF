# AIChatbotPDF
Build a chat app using a large language model. I net out how retrieval augmented generation builds on LLMs, then I show how custom data, like a PDF, can be loaded and used for more meaningful, insightful chat responses.

LeetCode Solution Bot - Project Explanation
Project Overview
This is a Retrieval-Augmented Generation (RAG) based chatbot specifically designed to provide solutions to LeetCode problems. It combines the power of large language models with your personal collection of LeetCode solutions stored in a PDF document.

How It Works
Document Processing:
The application loads your Leetcode.pdf file containing solutions
It splits the document into manageable chunks using text splitting
These chunks are converted into numerical vectors (embeddings) for efficient searching
Query Processing:
When you ask a question, the system searches through the document chunks
It finds the most relevant sections containing similar information
These relevant sections are then used as context for generating an answer
Response Generation:
The system uses Groq's LLM (Language Model) to generate responses
The model is instructed to only use information from the provided document
If the answer isn't found in the document, it will say so instead of making up information
Key Components
User Interface:
Built with Streamlit for a clean, web-based chat interface
Maintains conversation history during the session
Backend:
Uses LangChain for document processing and retrieval
Implements vector search to find relevant information
Integrates with Groq's API for fast LLM inference
Knowledge Base:
Your Leetcode.pdf serves as the knowledge base
The system only provides answers based on this document
Why This Approach?
Accuracy: By grounding responses in your document, it provides more accurate solutions
Privacy: Your solutions stay on your machine (the PDF is processed locally)
Customization: You can update the knowledge base by simply modifying the PDF
Ideal Use Case
This bot is perfect for:

Quickly looking up solutions you've previously worked on
Reviewing different approaches to problems
Studying for technical interviews
Maintaining a personal knowledge base of coding solutions
Limitations
The quality of answers depends on the content of your PDF
It can only answer questions about problems that are included in your document
The system requires an internet connection to access the Groq API
Future Enhancements
Support for multiple document formats
Adding code execution to test solutions
Implementing user authentication
Adding support for different programming languages
Including problem difficulty levels and categorie
