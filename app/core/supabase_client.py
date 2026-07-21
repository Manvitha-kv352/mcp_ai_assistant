from supabase import create_client, Client
from app.core.settings import settings


class SupabaseClient:

    def __init__(self):

        self.client: Client = create_client(
            settings.supabase_url,
            settings.supabase_key
        )


    def table(self, table_name: str):

        return self.client.table(table_name)


# Global Supabase instance
supabase_client = SupabaseClient()