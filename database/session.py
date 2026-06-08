from sqlalchemy.ext.asyncio import async_sessionmaker
from database.connection import engine

SessionLocal = async_sessionmaker(
    bind=engine  ,
    expire_on_commit=False,
    autoflush=False,
    autocommit=False,
)  


#create session Per database interaction