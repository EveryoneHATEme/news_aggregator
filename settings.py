import os
from pathlib import Path
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

if os.path.exists(Path(__file__).parent / ".env"):
    load_dotenv(".env")


class Settings(BaseSettings):
    TG_API_ID: int
    TG_API_HASH: str


settings = Settings()
