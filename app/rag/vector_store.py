import chromadb

from app.rag.embeddings import EmbeddingModel


class VectorStore:

    def __init__(self):
        self.client = chromadb.PersistentClient(path="./chroma_db")

        self.collection = self.client.get_or_create_collection(
            name="documents"
        )

        self.embedding_model = EmbeddingModel()

    def add_documents(self, chunks):

        ids = []
        embeddings = []

        for i, chunk in enumerate(chunks):
            ids.append(str(i))
            embeddings.append(
                self.embedding_model.embed_text(chunk)
            )

        self.collection.add(
            ids=ids,
            documents=chunks,
            embeddings=embeddings
        )

    def search(self, query, top_k=3):

        query_embedding = self.embedding_model.embed_text(query)

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )

        return results["documents"][0]