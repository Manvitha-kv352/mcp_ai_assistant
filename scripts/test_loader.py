print(">>> NEW TEST LOADER <<<")

from app.rag.loader import DocumentLoader


def main():
    loader = DocumentLoader()

    text = loader.load_pdf(
        r"C:\Users\MANVITH\OneDrive\Desktop\mcp-assistant\Manvitha_KV_Resume.pdf"
    )

    print(text)


if __name__ == "__main__":
    main()