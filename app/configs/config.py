import os
from pydantic_settings import BaseSettings

ENVIRONMENT = os.getenv("ENVIRONMENT", "local")

class Settings(BaseSettings):
    database_url: str
    secret_key: str
    access_token_expire_minutes: int = 30

    class Config:
        env_file = f"app/configs/{ENVIRONMENT}.env"

settings = Settings()