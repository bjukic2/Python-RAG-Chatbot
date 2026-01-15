# RAG Chatbot - FastAPI + Next.js

An interactive chatbot powered by **Retrieval-Augmented Generation (RAG)**, built with **FastAPI backend** and a **Next.js** frontend.
The system retrieves relevant documents from a local vector database (**ChromaDB**) and generates context-aware answers through a custom RAG pipeline. It uses local open-source **llama3-1** model, so it can answer some general knowledge questions without needing any external documents.

The project is split into two independent parts:

- **backend/** - FastAPI, RAG pipeline, ChromaDB, ingestion scripts
- **frontend/** - Next.js chat interface

---

## Features

- **RAG pipeline** for document retrieval
- **FastAPI backend** with clean modular architecture
- **Next.js chat UI** with loading animation and message history
- **Real-time communication** between frontend and backend
- **Embeddings + vector search** via ChromaDB
- **CORS-enabled** for safe frontend <-> backend communication
- **Easily extendable** for new models, data sources or UI features

---

## Getting started

### 1. Clone the repo

```bash
# In terminal
git clone https://github.com/bjukic2/Python-RAG-Chatbot.git

# Navigate to the project folder
cd Python-RAG-Chatbot
```

### 2. Install dependencies

```bash
# Install dependencies for backend
cd backend/
source venv/bin/activate
pip install -r requirements.txt

# Return to previous folder
cd ..

# Install dependencies for frontend
cd frontend/
npm install

# Return to previous folder
cd ..
```

### 3. Installing Llama using Ollama

```bash
curl -fsSL https://ollama.com/install.sh | sudo sh
ollama pull llama3.1
ollama run llama3.1
```

### 4. Run the project

```bash
# Open two terminals

# In terminal one run backend
cd backend/
uvicorn main:app --reload

# In terminal two run frontend
cd frontend/
npm run dev
```

### 5. Use the chatbot

Open http://localhost:3000 and type your question in the **text field and press** "**Send**"

---

## Author

Made by **Bruno Jukić** [https://github.com/bjukic2]
