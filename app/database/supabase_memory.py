from app.database.supabase_client import supabase


class AgentMemory:

    def save(self, agent, key, value):

        supabase.table("agent_memory").insert(
            {
                "agent": agent,
                "memory_key": key,
                "memory_value": value,
            }
        ).execute()

    def load(self, agent):

        response = (
            supabase.table("agent_memory")
            .select("*")
            .eq("agent", agent)
            .execute()
        )

        return response.data