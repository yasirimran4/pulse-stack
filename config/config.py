from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_env
import os
load_env()
# All configrations

DATABASE_URL = os.getenv("DATABASE_URL")
class Settings(BaseSettings):
    # JWT Configuration
    DATABASE_URL : str | None = DATABASE_URL 
    SECRET_KEY : str = "my_n@me_y@asir.?"
    ALGORITHM : str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES : int = 30

    model_config = SettingsConfigDict(
        env_file='.env',
        extra= 'ignore'
    )

settings = Settings()

