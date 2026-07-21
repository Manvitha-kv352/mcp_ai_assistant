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
You are a helpful AI assistant.

Use the provided context when it is relevant. If the context is limited or unrelated, answer the question naturally and generally from your own knowledge.

Context:

{retrieved_context}

Question:

{question}

Answer:
"""
        else:
            prompt = f"""
You are a helpful AI assistant.

Answer the user's question directly and generally. If the user is asking for casual conversation, be conversational. If they ask for factual information, provide a clear general answer.
Do not mention uploaded documents unless the user explicitly asks about them.

Question:

{question}

Answer:
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