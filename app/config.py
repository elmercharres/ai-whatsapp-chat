from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    ENV: str = "dev"
    DATABASE_URL: str

    OPENAI_API_KEY: str
    ANTHROPIC_API_KEY: str
    GEMINI_API_KEY: str

    WHATSAPP_PROVIDER: str = "twilio"

    class Config:
        env_file = ".env"

settings = Settings()
