# RAG Chatbot - FastAPI + Next.js

An interactive chatbot powered by **Retrieval-Augmented Generation (RAG)**, built with **FastAPI backend** and a **Next.js** frontend.
The system retrieves relevant documents from a local vector database (**ChromaDB**) and generates context-aware answers through a custom RAG pipeline. It uses open-source **llama3-1** model, so it can answer some general knowledge questions without needing any external documents.

The project is split into two independent parts:

- backend/ - FastAPI, RAG pipeline, ChromaDB, ingestion scripts
- frontend/ - Next.js chat interface

---

# Features

- **RAG pipeline** for document retrieval
- **FastAPI backend** with clean modular architecture
- **Next.js chat UI** with loading animation and message history
- **Real-time communication** between frontend and backend
- **Embeddings + vector search** via ChromaDB
- **CORS-enabled** for safe frontend <-> backend communication
- **Easily extendable** for new models, data sources or UI features
