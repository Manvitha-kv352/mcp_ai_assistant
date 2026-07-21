from app.rag.retriever import Retriever


def main():
    retriever = Retriever()

    query = "What are Manvitha's technical skills?"

    results = retriever.retrieve(query)

    print("\nRetrieved Chunks:\n")

    for i, chunk in enumerate(results, start=1):
        print(f"Chunk {i}")
        print("-" * 50)
        print(chunk)
        print()


if __name__ == "__main__":
    main()