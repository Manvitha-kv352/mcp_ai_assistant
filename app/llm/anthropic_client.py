import anthropic

from app.core.settings import settings


class AnthropicClient:

    def __init__(self):
        self.client = anthropic.Anthropic(
            api_key=settings.anthropic_api_key
        )

    def chat(self, message: str) -> str:
        response = self.client.messages.create(
            model=settings.model_name,
            max_tokens=300,
            messages=[
                {
                    "role": "user",
                    "content": message
                }
            ]
        )

        return response.content[0].text