from sqlalchemy import Column , String , Integer , Boolean , DateTime
from database.connection import Base
from sqlalchemy.sql import func

class User(Base):

    __tablename__ = "users"

    id = Column(Integer,primary_key=True,index=True)
    name = Column(String(100),nullable=False)
    email = Column(String(100),unique=True,nullable=False,index=True)
    hashed_password = Column(String(255),nullable=False)
    role = Column(String(100),default="user")
    is_active = Column(Boolean,default=True)
    created_at = Column(DateTime(timezone=True),server_default = func.now())
    updated_at = Column(DateTime(timezone=True),onupdate = func.now(),nullable=True)


