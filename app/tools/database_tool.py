from app.database.supabase_client import supabase


class DatabaseTool:

    def save_chat(self, session_id, role, message):

        supabase.table("chat_history").insert({
            "session_id": session_id,
            "role": role,
            "message": message
        }).execute()

        return "saved"


    def load_chat(self, session_id):

        response = (
            supabase
            .table("chat_history")
            .select("*")
            .eq("session_id", session_id)
            .order("created_at")
            .execute()
        )

        return response.data


    def save_memory(self, key, value):

        supabase.table("agent_memory").insert({
            "memory_key": key,
            "memory_value": value
        }).execute()

        return "memory saved"


    def load_memory(self, key):

        response = (
            supabase
            .table("agent_memory")
            .select("*")
            .eq("memory_key", key)
            .execute()
        )

        return response.data