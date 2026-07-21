from app.tools.database_tool import DatabaseTool
from app.tools.file_tool import FileTool
from app.tools.api_tool import APITool


class ToolRegistry:

    def __init__(self):

        self.tools = {
            "database": DatabaseTool(),
            "file": FileTool(),
            "api": APITool(),
        }

    def get(self, name):
        return self.tools.get(name)