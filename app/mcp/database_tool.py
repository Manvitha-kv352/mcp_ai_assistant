from app.core.supabase_client import supabase_client


class DatabaseTool:


    async def execute(self, data: dict):

        action = data.get("action")

        table = data.get("table")


        if not table:
            raise ValueError(
                "Table name required"
            )


        if action == "insert":

            payload = data.get("data")

            response = (
                supabase_client
                .table(table)
                .insert(payload)
                .execute()
            )

            return response.data



        elif action == "select":

            response = (
                supabase_client
                .table(table)
                .select("*")
                .execute()
            )

            return response.data



        elif action == "update":

            payload = data.get("data")
            match = data.get("match")


            response = (
                supabase
                .table(table)
                .update(payload)
                .match(match)
                .execute()
            )

            return response.data



        elif action == "delete":

            match = data.get("match")


            response = (
                supabase_client
                .table(table)
                .delete()
                .match(match)
                .execute()
            )

            return response.data



        else:

            raise ValueError(
                f"Unknown database action: {action}"
            )