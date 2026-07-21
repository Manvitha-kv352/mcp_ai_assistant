from app.llm.ollama_client import OllamaClient


class ReviewerAgent:

    def __init__(self):
        self.llm = OllamaClient()

    def review(self, question: str, answer: str):

        prompt = f"""
You are an expert AI Reviewer.

Review the following answer.

Your tasks:
1. Check whether the answer correctly addresses the user's question.
2. Check whether the answer is clear and complete.
3. If the answer is already good, return it unchanged.
4. If improvements are needed, rewrite the answer.

User Question:
{question}

Generated Answer:
{answer}

Final Reviewed Answer:
"""

        return self.llm.chat(prompt)