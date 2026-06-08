from pydantic_settings import BaseSettings, SettingsConfigDict

# All configrations
class Settings(BaseSettings):
    # JWT Configuration
    DATABASE_URL : str = "postgresql+asyncpg://neondb_owner:npg_jkr1NJvtZ2uR@ep-misty-smoke-apt068uz-pooler.c-7.us-east-1.aws.neon.tech/neondb"
    SECRET_KEY : str = "my_n@me_y@asir.?"
    ALGORITHM : str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES : int = 30

    model_config = SettingsConfigDict(
        env_file='.env',
        extra= 'ignore'
    )

settings = Settings()

