import requests
from app.rag.embedder import Embedder
from app.db.vector_store import VectorStore

class RAGPipeline:
    def __init__(self, model_name: str = "llama3.1"):
        self.embedder = Embedder()
        self.store = VectorStore()
        self.model = model_name   # Ollama chat model

    def run(self, query: str) -> str:
        # 1) Embedding upit
        query_embedding = self.embedder.embed(query)

        # 2) Vector search
        results = self.store.query(query_embedding, n_results=4)
        retrieved_docs = results["documents"][0] if results["documents"] else []
        context = "\n\n".join(retrieved_docs)

        # 3) Prompt
        prompt = f"""Odgovaraj kratko, jasno i prirodno, bez nepotrebnih objašnjenja.
Ako kontekst ne sadrži odgovor, reci samo "Ne znam".


Kontekst:
{context}

Pitanje korisnika:
{query}

Odgovor:
"""

        # 4) Ollama chat poziv
        response = requests.post(
            "http://localhost:11434/api/chat",
            json={
                "model": self.model,
                "messages": [
                    {"role": "system", "content": "Ti si stručni AI asistent."},
                    {"role": "user", "content": prompt}
                ],
                "stream": False
            }
        )

        data = response.json()
        return data["message"]["content"]
