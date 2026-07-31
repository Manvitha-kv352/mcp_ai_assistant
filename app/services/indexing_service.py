from app.rag.loader import DocumentLoader
from app.rag.chunker import TextChunker
from app.rag.vector_store import VectorStore


class IndexingService:

    def __init__(self):
        self.loader = DocumentLoader()
        self.chunker = TextChunker()
        self.vector_store = VectorStore()

    def index_pdf(self, file_path: str):
        try:
            text = self.loader.load_document(file_path)
        except Exception as exc:
            raise ValueError(f"Failed to load document file: {exc}") from exc

        if not text or not text.strip():
            return 0

        chunks = self.chunker.chunk_text(text)

        if not chunks:
            return 0

        self.vector_store.add_documents(chunks)

        return len(chunks)