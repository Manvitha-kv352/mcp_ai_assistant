import httpx


class APITool:

    async def get(self, url: str):

        async with httpx.AsyncClient() as client:

            response = await client.get(url)

            response.raise_for_status()

            return response.json()