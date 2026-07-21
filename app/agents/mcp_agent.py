from app.agents.base_agent import BaseAgent
from app.mcp.router import MCPRouter


class MCPAgent(BaseAgent):

    def __init__(self):

        self.router = MCPRouter()


    async def execute(
        self,
        task,
        context
    ):

        tool = task.input.get("tool")

        method = task.input.get("method")

        data = task.input.get("data")


        result = await self.router.route(
            tool,
            method,
            data
        )


        # Save output if context supports it
        if hasattr(context, "add_output"):

            context.add_output(
                "MCP",
                result
            )


        return {
            "agent": "MCP",
            "status": "success",
            "result": result
        }