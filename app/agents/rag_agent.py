from app.agents.base_agent import BaseAgent
from app.rag.retriever import Retriever
from app.llm.ollama_client import OllamaClient


class RAGAgent(BaseAgent):

    def __init__(self):

        self.retriever = Retriever()
        self.llm = OllamaClient()


    async def execute(self, task, context):

        # Get user query from Task
        question = task.input


        # Retrieve documents when available
        try:
            chunks = self.retriever.retrieve(question)
        except Exception:
            chunks = []

        retrieved_context = "\n\n".join(
            [str(chunk) for chunk in chunks if str(chunk).strip()]
        )

        if retrieved_context.strip():
            prompt = f"""
You are a helpful, conversational AI assistant.

Use the provided context when it is relevant. If the context is limited or unrelated, answer in a friendly, natural way based on your own knowledge.
If the user input is short, like "next" or "okay", continue the conversation smoothly and do not ask them to rephrase as a question.
Do not mention uploaded documents unless the user explicitly asks about them.

Context:

{retrieved_context}

User:
{question}

Assistant:
"""
        else:
            prompt = f"""
You are a helpful, conversational AI assistant.

Answer naturally and clearly, even when the user input is short or informal.
If the user asks casually or says something like "next" or "okay", continue the conversation without demanding a formal question.
If the user asks for factual information, provide a clear answer. If the user wants chat, respond in a friendly way.
Do not mention uploaded documents unless the user explicitly asks about them.

User:
{question}

Assistant:
"""

        response = self.llm.chat(prompt)


        result = {
            "agent": "RAG",
            "status": "success",
            "result": response,
            "metadata": {
                "chunks_retrieved": len(chunks) if isinstance(chunks, list) else 0
            }
        }


        if hasattr(context, "add_output"):

            context.add_output(
                "RAG",
                response
            )


        return result