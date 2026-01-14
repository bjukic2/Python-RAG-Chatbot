from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    openai_api_key: str | None = None

    embedding_model_name: str = "text-embedding-3-small"
    chat_model_name: str = "gpt-4.1-mini"

    vector_store_path: str = "data/vector_store"

    class Config:
        env_file = ".env"

settings = Settings()