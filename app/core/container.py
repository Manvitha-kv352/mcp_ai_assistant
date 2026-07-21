from app.agents.agent_registry import AgentRegistry
from app.agents.rag_agent import RAGAgent
from app.agents.api_agent import APIAgent
from app.agents.database_agent import DatabaseAgent
from app.agents.llm_agent import LLMAgent
from app.agents.reviewer_agent import ReviewerAgent
from app.agents.mcp_agent import MCPAgent


def create_registry():

    registry = AgentRegistry()

    registry.register("RAG", RAGAgent())
    registry.register("API", APIAgent())
    registry.register("DATABASE", DatabaseAgent())
    registry.register("LLM", LLMAgent())
    registry.register("REVIEWER", ReviewerAgent())
    registry.register("MCP", MCPAgent())

    return registry
