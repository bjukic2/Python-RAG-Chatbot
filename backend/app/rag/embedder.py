import requests

class Embedder:
    def __init__(self, model_name: str = "nomic-embed-text"):
        self.model_name = model_name

    def embed(self, text: str) -> list[float]:
        response = requests.post(
            "http://localhost:11434/api/embeddings",
            json={
                "model": self.model_name,
                "prompt": text
            }
        )
        data = response.json()
        return data["embedding"]
