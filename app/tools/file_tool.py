from pathlib import Path


class FileTool:

    def read_file(self, filepath: str):

        path = Path(filepath)

        if not path.exists():
            raise FileNotFoundError(filepath)

        return path.read_text(encoding="utf-8")


    def write_file(self, filepath: str, content: str):

        path = Path(filepath)

        path.parent.mkdir(parents=True, exist_ok=True)

        path.write_text(content, encoding="utf-8")

        return {
            "status": "success",
            "file": filepath
        }


    def append_file(self, filepath: str, content: str):

        path = Path(filepath)

        path.parent.mkdir(parents=True, exist_ok=True)

        with open(path, "a", encoding="utf-8") as f:
            f.write(content)

        return {
            "status": "success",
            "file": filepath
        }


    def delete_file(self, filepath: str):

        path = Path(filepath)

        if path.exists():
            path.unlink()

        return {
            "status": "deleted"
        }