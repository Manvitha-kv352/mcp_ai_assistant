import ollama


class OllamaClient:

    def __init__(self):
        self.model = "llama3"

    def chat(self, prompt: str):

        response = ollama.chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]