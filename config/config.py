from pydantic_settings import BaseSettings, SettingsConfigDict

# All configrations
class Settings(BaseSettings):
    # JWT Configuration

    secret_key :str = "my_n@me_y@asir.?"
    database_url : str = "sqlite:///./data/users.db"
    token_expiry_time_minutes : int = 30
    algorithm : str = 'HS256'

    model_config = SettingsConfigDict(
        env_file='.env',
        extra='ignore'
    )

settings = Settings()

