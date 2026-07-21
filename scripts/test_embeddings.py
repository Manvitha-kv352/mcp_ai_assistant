from app.rag.embeddings import EmbeddingModel


def main():
    model = EmbeddingModel()

    vector = model.embed_text(
        "Artificial Intelligence is transforming healthcare."
    )

    print(f"Embedding length: {len(vector)}")
    print(vector[:10])


if __name__ == "__main__":
    main()