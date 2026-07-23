from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    app_name: str = "MCP Assistant"
    app_version: str = "0.1.0"

    # Supabase
    supabase_url: str = ""
    supabase_key: str = ""

    # LLM / API providers
    model_name: str = "llama-3.3-70b-versatile"
    groq_api_key: str = ""
    grok_api_key: str = ""
    groq_model: str = "llama-3.3-70b-versatile"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
        env_file_encoding="utf-8"
    )


settings = Settings()