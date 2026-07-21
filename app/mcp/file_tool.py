import os


class FileTool:

    async def execute(self, data: dict):

        action = data.get("action")

        if action == "read":

            path = data.get("path")

            if not os.path.exists(path):
                raise FileNotFoundError(path)

            with open(
                path,
                "r",
                encoding="utf-8"
            ) as file:
                return file.read()


        elif action == "write":

            path = data.get("path")
            content = data.get("content", "")

            with open(
                path,
                "w",
                encoding="utf-8"
            ) as file:
                file.write(content)

            return {
                "status": "success",
                "message": f"{path} created"
            }


        else:

            raise ValueError(
                f"Unknown file action: {action}"
            )