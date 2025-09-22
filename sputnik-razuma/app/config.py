from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    TELEGRAM_BOT_TOKEN: str
    OPENAI_API_KEY: str
    OPENAI_ASSISTANT_ID: str
    PUBLIC_BASE_URL: str | None = None
    WEBHOOK_SECRET: str | None = None
    ENV: str = "dev"
    TZ: str = "Europe/Oslo"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()  # raises if required missing
