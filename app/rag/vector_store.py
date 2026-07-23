import chromadb
import uuid

from app.rag.embeddings import EmbeddingModel


class VectorStore:

    def __init__(self):
        self.client = chromadb.PersistentClient(path="./chroma_db")

        self.collection = self.client.get_or_create_collection(
            name="documents"
        )

        self.embedding_model = EmbeddingModel()

    def add_documents(self, chunks):

        if not chunks:
            return

        ids = []
        documents = []
        embeddings = []

        for chunk in chunks:
            embedding = self.embedding_model.embed_text(chunk)
            if not isinstance(embedding, list) or len(embedding) == 0:
                continue

            ids.append(str(uuid.uuid4()))
            documents.append(chunk)
            embeddings.append(embedding)

        if not embeddings:
            return

        try:
            self.collection.add(
                ids=ids,
                documents=documents,
                embeddings=embeddings
            )
        except Exception as exc:
            raise RuntimeError(f"Failed to add documents to vector store: {exc}") from exc

    def search(self, query, top_k=3):

        query_embedding = self.embedding_model.embed_text(query)

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )

        return results["documents"][0]