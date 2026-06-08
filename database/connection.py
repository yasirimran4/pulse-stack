from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from config.config import settings

engine = create_engine(
    settings.database_url,
    echo=True,
    connect_args={"check_same_thread":False}
)


Base = declarative_base()
