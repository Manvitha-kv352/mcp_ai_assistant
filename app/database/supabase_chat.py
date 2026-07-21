from app.database.supabase_client import get_supabase_client


class SupabaseChatDB:

    def _get_client(self):
        return get_supabase_client()

    def save_message(
        self,
        session_id,
        role,
        message,
    ):
        client = self._get_client()
        if client is None:
            return None

        client.table("chat_history").insert(
            {
                "session_id": session_id,
                "role": role,
                "message": message,
            }
        ).execute()

    def get_history(self, session_id):
        client = self._get_client()
        if client is None:
            return []

        response = (
            client.table("chat_history")
            .select("*")
            .eq("session_id", session_id)
            .order("created_at")
            .execute()
        )

        return response.data