from app.mcp.api_tool import APITool
from app.mcp.file_tool import FileTool
from app.mcp.database_tool import DatabaseTool


class MCPServer:

    def __init__(self):

        self.tools = {
            "api": APITool(),
            "file": FileTool(),
            "database": DatabaseTool()
        }


    def list_tools(self):

        return list(self.tools.keys())


    def get_tool(self, name):

        return self.tools.get(name)


    async def execute(
        self,
        tool_name: str,
        method_name: str,
        *args,
        **kwargs
    ):

        tool = self.get_tool(tool_name)

        if tool is None:
            raise ValueError(
                f"Tool '{tool_name}' not found"
            )


        method = getattr(
            tool,
            method_name,
            None
        )


        if method is None:
            raise ValueError(
                f"Tool '{tool_name}' has no method '{method_name}'"
            )


        return await method(
            *args,
            **kwargs
        )