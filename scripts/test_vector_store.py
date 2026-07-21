from app.rag.loader import DocumentLoader
from app.rag.chunker import TextChunker
from app.rag.vector_store import VectorStore


def main():

    loader = DocumentLoader()
    chunker = TextChunker()
    store = VectorStore()

    text = loader.load_pdf(
        r"C:\Users\MANVITH\OneDrive\Desktop\mcp-assistant\Manvitha_KV_Resume.pdf"
    )

    chunks = chunker.chunk_text(text)

    store.add_documents(chunks)

    results = store.search("What are Manvitha's skills?")

    print("\n===== SEARCH RESULTS =====\n")

    for result in results:
        print(result)
        print("-" * 50)


if __name__ == "__main__":
    main()