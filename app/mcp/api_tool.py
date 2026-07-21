import httpx


class APITool:

    async def execute(self, data: dict):
        if not isinstance(data, dict):
            raise ValueError("APITool expects a dictionary payload")

        method = data.get("method", "GET")
        url = data.get("url")

        if not url:
            raise ValueError("APITool requires a 'url' field in the payload")

        async with httpx.AsyncClient() as client:
            response = await client.request(method, url)
            response.raise_for_status()
            try:
                return response.json()
            except ValueError:
                return {"text": response.text}
