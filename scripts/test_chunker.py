from app.rag.loader import DocumentLoader
from app.rag.chunker import TextChunker


def main():
    loader = DocumentLoader()
    chunker = TextChunker()

    text = loader.load_pdf(
        r"C:\Users\MANVITH\OneDrive\Desktop\mcp-assistant\Manvitha_KV_Resume.pdf"
    )

    chunks = chunker.chunk_text(text)

    print(f"Number of chunks: {len(chunks)}")

    for i, chunk in enumerate(chunks, start=1):
        print(f"\n===== Chunk {i} =====")
        print(chunk)


if __name__ == "__main__":
    main()