import asyncio

from app.mcp.server import MCPServer


async def main():

    server = MCPServer()


    result = await server.execute(
        "file",
        "execute",
        {
            "action": "write",
            "path": "test.txt",
            "content": "MCP File Tool Working"
        }
    )

    print(result)


    result = await server.execute(
        "file",
        "execute",
        {
            "action": "read",
            "path": "test.txt"
        }
    )

    print(result)


asyncio.run(main())