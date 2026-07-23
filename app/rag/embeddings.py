from app.llm.ollama_client import OllamaClient


class EmbeddingModel:

    def __init__(self):
        self.client = OllamaClient()

    def embed_text(self, text: str):
        return self.client.embed_text(text)