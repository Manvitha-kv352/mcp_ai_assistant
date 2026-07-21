from app.mcp.server import MCPServer


class MCPRouter:

    def __init__(self):

        self.server = MCPServer()


    async def route(
        self,
        tool_name: str,
        method: str,
        payload
    ):

        return await self.server.execute(
            tool_name,
            method,
            payload
        )