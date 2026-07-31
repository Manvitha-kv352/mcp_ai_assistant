from pathlib import Path

from PyPDF2 import PdfReader


class DocumentLoader:

    def load_document(self, file_path: str) -> str:
        suffix = Path(file_path).suffix.lower()

        if suffix in {".txt", ".md", ".csv", ".json", ".yaml", ".yml"}:
            return Path(file_path).read_text(encoding="utf-8", errors="ignore")

        reader = PdfReader(file_path)
        text = ""

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        return text

    def load_pdf(self, file_path: str) -> str:
        return self.load_document(file_path)