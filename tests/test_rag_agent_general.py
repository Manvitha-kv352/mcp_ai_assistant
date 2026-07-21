import asyncio
import pytest

from app.agents.rag_agent import RAGAgent
from app.process.task import Task


class DummyContext:
    def __init__(self):
        self.outputs = {}

    def add_output(self, agent_name, output):
        self.outputs[agent_name] = output


class DummyRetriever:
    def __init__(self):
        self.calls = []

    def retrieve(self, query):
        self.calls.append(query)
        return []


class DummyLLM:
    def chat(self, prompt):
        return "General answer"


@pytest.mark.asyncio
async def test_rag_agent_falls_back_to_general_answer_when_no_context(monkeypatch):
    agent = RAGAgent()
    agent.retriever = DummyRetriever()
    agent.llm = DummyLLM()

    task = Task(agent="RAG", input_data="Hello there", task_type="rag")
    context = DummyContext()

    result = await agent.execute(task, context)

    assert result["status"] == "success"
    assert result["result"] == "General answer"
    assert context.outputs["RAG"] == "General answer"
