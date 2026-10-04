# 📄 Document Q&A Chatbot

An AI-powered Document Question & Answer chatbot that allows users to ask questions about uploaded documents and receive relevant answers using Retrieval-Augmented Generation (RAG).

## 🚀 Features

* Upload and process documents
* Split documents into smaller chunks
* Generate vector embeddings
* Retrieve relevant document content
* Ask questions using natural language
* Generate answers using an LLM
* Local AI processing using Ollama

## 🧠 How It Works

The chatbot follows a simple RAG pipeline:

```text
Document
   ↓
Text Extraction
   ↓
Chunking
   ↓
Embeddings
   ↓
Vector Search
   ↓
Relevant Context
   ↓
Ollama LLM
   ↓
Answer
```

## 🛠️ Technologies Used

* Python
* Streamlit
* Sentence Transformers
* Ollama
* Llama 3.2
* Retrieval-Augmented Generation (RAG)
* Vector Embeddings

## 📁 Project Structure

```text
document-qna-chatbot/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── ...
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd document-qna-chatbot
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

### 3. Activate the virtual environment

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Install Ollama

Install Ollama separately on your computer and make sure it is running.

Then pull the required model:

```bash
ollama pull llama3.2
```

### 6. Run the application

```bash
python3 -m streamlit run app.py
```

The application will open in your browser.

## 🤖 AI Model

This project uses **Llama 3.2 through Ollama** for local AI inference.

The Ollama model itself is **not included in this repository**. Users should install Ollama and download the model separately.

## 📌 Note

This project is intended for learning and demonstration of Retrieval-Augmented Generation, document processing, embeddings, and local LLM applications.

## 👩‍💻 Author

**Khushi Jagad**

GitHub: @khushinjagad
