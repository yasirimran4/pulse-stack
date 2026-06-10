from sqlalchemy import Column , String , Integer , Boolean , DateTime ,Enum as SQLEnum
from database.connection import Base
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship 
from enum import Enum

class UserRole(str,Enum):
    ADMIN = "admin"
    USER = "user"

class User(Base):

    __tablename__ = "users"

    id = Column(Integer,primary_key=True,index=True)
    name = Column(String(100),nullable=False)
    email = Column(String(100),unique=True,nullable=False,index=True)
    hashed_password = Column(String(255),nullable=False)
    role = Column(SQLEnum(UserRole),default=UserRole.USER,nullable=False)
    is_verified = Column(Boolean,default=False)
    is_active = Column(Boolean,default=True)
    created_at = Column(DateTime(timezone=True),server_default = func.now())
    updated_at = Column(DateTime(timezone=True),server_default = func.now(),onupdate = func.now(),nullable=True)
    
    # Relationships
    monitors = relationship("Monitor",back_populates="user",cascade="all, delete-orphan")


