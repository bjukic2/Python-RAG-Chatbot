import json
import httpx
from app.rag.embedder import Embedder
from app.db.vector_store import VectorStore

class RAGPipeline:
    def __init__(self, model_name: str = "llama3.1"):
        self.embedder = Embedder()
        self.store = VectorStore()
        self.model = model_name

    async def run_stream(self, query: str):
        # 1) Embedding
        query_embedding = self.embedder.embed(query)

        # 2) Vector search
        results = self.store.query(query_embedding, n_results=4)
        retrieved_docs = results["documents"][0] if results["documents"] else []
        context = "\n\n".join(retrieved_docs)

        # 3) Prompt
        prompt = f"""Odgovaraj kratko, jasno i prirodno.
Ako kontekst ne sadrži odgovor, reci "Ne znam".

Kontekst:
{context}

Pitanje:
{query}

Odgovor:
"""

        # 4) STREAMING preko /api/chat
        async with httpx.AsyncClient(timeout=None) as client:
            async with client.stream(
                "POST",
                "http://localhost:11434/api/chat",
                json={
                    "model": self.model,
                    "messages": [
                        {"role": "system", "content": "Ti si stručni AI asistent."},
                        {"role": "user", "content": prompt}
                    ],
                    "stream": True
                }
            ) as response:

                full_text = ""

                async for line in response.aiter_lines():
                    if not line:
                        continue

                    try:
                        obj = json.loads(line)
                        content = obj["message"]["content"]

                        # izračunaj razliku (Ollama šalje growing prefix)
                        if content.startswith(full_text):
                            diff = content[len(full_text):]
                        else:
                            diff = content

                        full_text = content

                        if diff:
                            yield json.dumps({
                                "message": {"role": "assistant", "content": diff}
                            }) + "\n"

                    except:
                        continue
