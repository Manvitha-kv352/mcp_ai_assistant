import asyncio

from app.tools.api_tool import APITool


async def main():

    api = APITool()

    data = await api.get(
        "https://jsonplaceholder.typicode.com/posts/1"
    )

    print(data)


asyncio.run(main())