import asyncio

from app.mcp.server import MCPServer


async def main():

    server = MCPServer()

    print(server.list_tools())


    result = await server.execute(
        "database",
        "execute",
        {
            "action": "select",
            "table": "agent_memory"
        }
    )


    print(result)


asyncio.run(main())