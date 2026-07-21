from app.rag.loader import DocumentLoader
from app.rag.chunker import TextChunker
from app.rag.vector_store import VectorStore


class IndexingService:

    def __init__(self):
        self.loader = DocumentLoader()
        self.chunker = TextChunker()
        self.vector_store = VectorStore()

    def index_pdf(self, file_path: str):

        text = self.loader.load_pdf(file_path)

        chunks = self.chunker.chunk_text(text)

        self.vector_store.add_documents(chunks)

        return len(chunks)