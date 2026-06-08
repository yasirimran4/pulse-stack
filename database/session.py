from sqlalchemy.orm import sessionmaker
from database.connection import engine

SessionLocal = sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine  
)  


#create session Per database interaction