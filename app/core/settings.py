from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    app_name: str = "MCP Assistant"
    app_version: str = "0.1.0"

    # Supabase
    supabase_url: str = ""
    supabase_key: str = ""
    model_name: str = "llama3"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()