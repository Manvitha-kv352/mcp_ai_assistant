import hashlib
import os

import requests

from app.core.settings import settings


class OllamaClient:

    def __init__(self):
        self.model = settings.groq_model or settings.model_name or "llama-3.3-70b-versatile"
        self.api_key = settings.groq_api_key or settings.grok_api_key or os.getenv("GROQ_API_KEY") or os.getenv("GROK_API_KEY") or ""
        self.base_url = "https://api.groq.com/openai/v1"

    def _headers(self):
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

    def chat(self, prompt: str):
        if not self.api_key:
            return "Groq API key is not configured. Please set GROQ_API_KEY or GROK_API_KEY in your environment."

        try:
            response = requests.post(
                f"{self.base_url}/chat/completions",
                headers=self._headers(),
                json={
                    "model": self.model,
                    "messages": [{"role": "user", "content": prompt}],
                    "temperature": 0.2,
                },
                timeout=60,
            )
            response.raise_for_status()
            payload = response.json()
            return payload["choices"][0]["message"]["content"]
        except Exception:
            return "The Groq service could not be reached, so I’m returning a fallback response."

    def embed_text(self, text: str):
        if not self.api_key:
            return self._fallback_embedding(text)

        try:
            response = requests.post(
                f"{self.base_url}/embeddings",
                headers=self._headers(),
                json={"input": text, "model": "text-embedding-3-small"},
                timeout=60,
            )
            response.raise_for_status()
            payload = response.json()
            embedding = None

            if isinstance(payload, dict):
                data = payload.get("data")
                if isinstance(data, list) and len(data) > 0:
                    first = data[0]
                    if isinstance(first, dict):
                        embedding = first.get("embedding") or first.get("embeddings")

            if isinstance(embedding, list) and len(embedding) > 0:
                return embedding

            return self._fallback_embedding(text)
        except Exception:
            return self._fallback_embedding(text)

    def _fallback_embedding(self, text: str):
        digest = hashlib.sha256(text.encode("utf-8")).digest()
        return [((digest[i % len(digest)] + (i * 17)) % 255) / 255.0 for i in range(768)]