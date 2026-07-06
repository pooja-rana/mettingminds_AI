from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "MeetingMind AI"
    environment: str = "development"
    database_url: str = "sqlite:///./meetingmind.db"
    openai_api_key: str | None = None
    chroma_collection: str = "meetingmind"
    host: str = "0.0.0.0"
    port: int = 8000

    class Config:
        env_file = ".env"


settings = Settings()
