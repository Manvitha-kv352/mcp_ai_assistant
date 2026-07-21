import asyncio

from app.agents.mcp_agent import MCPAgent
from app.process.task import Task
from app.context.context_manager import ContextManager


async def main():

    agent = MCPAgent()

    context = ContextManager()


    task = Task(
        agent="MCP",
        input_data={
            "tool": "api",
            "method": "execute",
            "data": {
                "url": "https://jsonplaceholder.typicode.com/posts/1"
            }
        }
    )


    result = await agent.execute(
        task,
        context
    )


    print(result)



asyncio.run(main())