# LeetCode Solution Bot

A RAG (Retrieval-Augmented Generation) based chatbot that provides solutions to LeetCode problems using a custom knowledge base.

## 🚀 Features

- Answers LeetCode problems using a custom knowledge base
- Maintains conversation history
- Uses Groq's LLM for generating responses
- Processes and retrieves information from PDF documents

## 🛠 How It Works

### Document Processing
- Loads your `Leetcode.pdf` file containing solutions
- Splits the document into manageable chunks
- Converts text into numerical vectors (embeddings) for efficient searching

### Query Handling
- Searches through document chunks when you ask a question
- Finds the most relevant sections containing similar information
- Uses these sections as context for generating accurate answers

### Response Generation
- Uses Groq's LLM to generate responses
- Strictly uses only the provided document context
- Clearly indicates when information isn't available in the knowledge base

## 📦 Prerequisites

- Python 3.8+
- Groq API key
- LeetCode solutions in PDF format

## 🚀 Installation

  Clone the repository:
   ```bash
   git clone <your-repository-url>
   cd <repository-name>

   python -m venv venv
# On Windows: venv\Scripts\activate
# On Unix/MacOS: source venv/bin/activate

pip install -r requirements.txt
pip install -r requirements.txt
GROQ_API_KEY=your_groq_api_key_here
streamlit run phase1.py


.
├── phase1.py          # Main application
├── Leetcode.pdf       # Your LeetCode solutions (not included)
├── .env               # Environment variables
├── requirements.txt   # Dependencies
└── README.md          # This file

