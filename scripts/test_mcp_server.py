import asyncio

from app.mcp.server import MCPServer


async def main():

    server = MCPServer()

    print(server.list_tools())


    result = await server.execute(
        "api",
        "execute",
        {
            "method": "GET",
            "url": "https://jsonplaceholder.typicode.com/posts/1"
        }
    )


    print(result)


asyncio.run(main())