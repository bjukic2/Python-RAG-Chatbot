from app.rag.embedder import Embedder
from app.db.vector_store import VectorStore
from app.utils.text_splitter import split_text

def ingest_documents(documents: list[str]):
    embedder = Embedder()
    store = VectorStore()

    ids = []
    texts = []
    embeddings = []

    for i, doc in enumerate(documents):
        chunks = split_text(doc)

        for j, chunk in enumerate(chunks):
            chunk_id = f"doc_{i}_chunk_{j}"
            ids.append(chunk_id)
            texts.append(chunk)
            embeddings.append(embedder.embed(chunk))

    store.add(ids, texts, embeddings)
    print("Ingest complete.")

if __name__ == "__main__":
    docs = [

    ]
    ingest_documents(docs)