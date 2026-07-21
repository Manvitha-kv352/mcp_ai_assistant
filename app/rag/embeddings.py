from ollama import embed


class EmbeddingModel:

    def __init__(self):
        self.model = "nomic-embed-text"

    def embed_text(self, text: str):
        response = embed(
            model=self.model,
            input=text
        )

        return response["embeddings"][0]