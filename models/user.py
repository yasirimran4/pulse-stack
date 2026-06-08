from sqlalchemy import Column , String , Integer , Boolean , DateTime , ForeignKey ,Text, Table
from database.connection import Base
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship , selectinload

class User(Base):

    __tablename__ = "users"

    id = Column(Integer,primary_key=True,index=True)
    name = Column(String(100),nullable=False)
    email = Column(String(100),unique=True,nullable=False,index=True)
    hashed_password = Column(String(255),nullable=False)
    role = Column(String(100),default="user")
    is_verified = Column(Boolean,default=False)
    is_active = Column(Boolean,default=True)
    created_at = Column(DateTime(timezone=True),server_default = func.now())
    updated_at = Column(DateTime(timezone=True),onupdate = func.now(),nullable=True)
    
    # Relationships
    monitors = relationship("Monitor",back_populates="user",cascade="all, delete-orphan")


class Monitor(Base):

    __tablename__ = "monitors"
    
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String,nullable=False)
    url = Column(String,unique=True,nullable=False,index=True)
    check_interval = Column(Integer,nullable=False)
    current_status = Column(String,nullable=True)
    is_active = Column(Boolean,default=True)
    checked_at = Column(DateTime(timezone=True),server_default = func.now())
    last_checked_at = Column(DateTime(timezone=True),server_default = func.now())

    # Foreign Key
    user_id = Column(Integer,ForeignKey("users.id"))

    # Relationships
    user = relationship("user",back_populates="monitors")
    monitor_check = relationship("MonitorChecks",back_populates="monitor",cascade="all, delete-orphan")

class MonitorChecks(Base):

    __tablename__ = "monitor_checks"
    id = Column(Integer,primary_key=True,index=True)
    monitor_id = Columns(Integer,ForeignKey("monitors.id"))









    
