from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_DB_PATH = PROJECT_ROOT / "mapzar.db"


class Settings(BaseSettings):
    bot_token: str
    database_url: str = f"sqlite:///{DEFAULT_DB_PATH}"

    # Reads from .env automatically at runtime
    model_config = SettingsConfigDict(
        env_file=PROJECT_ROOT / ".env",
        env_file_encoding="utf-8"
    )


# Instantiated directly: Pydantic handles validation & loading
settings = Settings()