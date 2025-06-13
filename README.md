# 📚 AI Chatbot with PDF Context Retrieval

This project is a **context-aware AI chatbot** that intelligently answers questions based *only* on the content of a given PDF document. It uses **LangChain**, **Groq’s Qwen model**, **Pinecone**, and **Hugging Face embeddings** to perform Retrieval-Augmented Generation (RAG) for document-based Q&A.

If a question is **out of context**, it responds with:
> “I don’t know based on the provided context.”

---

## 🚀 Demo Features

- ✅ Answers strictly based on PDF content
- 🔍 Uses semantic search with Pinecone
- 🧠 Integrated Groq LLM (Qwen-QWQ-32B)
- 📄 Processes and chunks PDF content using LangChain
- 🎤 Voice input support
- 🔊 Text-to-speech output for bot responses
- 🖼️ Modern UI with Bootstrap 4
- ⚙️ Flask backend with RESTful endpoint

---

## 🧠 Tech Stack

| Purpose         | Technology                                 |
|----------------|---------------------------------------------|
| Backend         | Flask, LangChain                           |
| Embeddings      | Hugging Face `all-MiniLM-L6-v2`            |
| Vector Store    | Pinecone                                    |
| LLM             | Groq `qwen-qwq-32b`                         |
| Frontend        | HTML, CSS, Bootstrap 4.6, jQuery, JS        |
| Voice & TTS     | Web Speech API                             |

---

## 📁 Project Structure

project-root/
│
├── app.py # Main Flask application
├── setup.py # Python package setup
├── .env # Environment variables (PINECONE & GROQ keys)
├── src/
│ ├── init.py
│ ├── helper.py # File loading, splitting, and embedding functions
│ ├── prompt.py # System prompt for chat logic
│
├── static/
│ └── style.css # UI styles
│
├── templates/
│ └── index.html # Main chat UI
│
├── Data/
│ └── your-pdf-file.pdf # The document used as context
└── research/
└── trials.ipynb # Optional experiments notebook


---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/lahiruCirclebook/AI_ChatBot.git
cd AI_ChatBot

python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows

pip install -r requirements.txt

PINECONE_API_KEY=your-pinecone-key
GROQ_API_KEY=your-groq-key

python app.py
The app will be available at http://localhost:8080.

📚 How It Works
PDF files are loaded and split into text chunks using LangChain's RecursiveCharacterTextSplitter.

Chunks are embedded using Hugging Face all-MiniLM-L6-v2.

Pinecone is used to store and retrieve similar chunks.

Groq's Qwen LLM generates an answer from the top k=3 relevant chunks.

If content is irrelevant, the bot replies with a default fallback message using a custom system prompt.

📌 System Prompt (Used for Grounding)
"You are a highly knowledgeable and concise AI assistant specialized in answering complex questions using the provided context. ... If the context does not contain enough information, respond with: 'I don't know based on the provided context.'"

🧪 Example Questions
✅ "What is a Markov Chain?"
→ Will return an accurate answer from the PDF.

❌ "Tell me 4 animals"
→ Will return: "I don't know based on the provided context."

