from app.llm.ollama_client import OllamaClient


class LLMAgent:

    def __init__(self):
        self.llm = OllamaClient()

    def run(self, message: str):
        return self.llm.chat(message)