import json

from app.llm.ollama_client import OllamaClient
from app.process.task import Task


class PlannerAgent:

    def __init__(self):

        self.llm = OllamaClient()


    def plan(self, user_query: str):

        prompt = f"""
You are an AI planner for an autonomous MCP assistant.

Your job is to select the correct agent.

Available agents:

1. RAG
Use for:
- general questions and conversation
- uploaded documents or PDFs when the user asks about them
- resume, reports, or stored files when relevant

2. MCP
Use when the user asks for:
- API calls
- URLs
- websites
- external data
- online information
- database operations
- file operations


MCP tools:

api:
- URLs
- external services
- online information


database:
- user memory
- chat history
- stored records


file:
- reading/writing files


IMPORTANT RULES:

If the user message contains:
"http://"
"https://"
"url"
"website"
"API"
"fetch"
"get online"
"external"

ALWAYS select MCP.


Return ONLY JSON.

Examples:


User:
"Tell me about my resume"

Output:
{{
    "agent":"RAG"
}}


User:
"Get data from https://jsonplaceholder.typicode.com/posts/1"

Output:
{{
    "agent":"MCP",
    "tool":"api",
    "method":"execute"
}}


User:
"Save my chat history"

Output:
{{
    "agent":"MCP",
    "tool":"database",
    "method":"execute"
}}


User request:

{user_query}

"""


        response = self.llm.chat(prompt)


        try:

            decision = json.loads(response)


        except Exception:

            decision = {
                "agent": "RAG"
            }


        agent = decision.get(
            "agent",
            "RAG"
        )


        # RAG task

        if agent == "RAG":

            return [
                Task(
                    agent="RAG",
                    input_data=user_query,
                    task_type="rag"
                )
            ]


        # MCP task

        elif agent == "MCP":

            return [
                Task(
                    agent="MCP",
                    input_data={
                        "tool": decision.get("tool"),
                        "method": decision.get("method"),
                        "data": {
                            "query": user_query
                        }
                    },
                    task_type="mcp"
                )
            ]


        # fallback

        return [
            Task(
                agent="RAG",
                input_data=user_query
            )
        ]