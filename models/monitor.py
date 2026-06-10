from sqlalchemy import Column , String , Integer , Boolean , DateTime , ForeignKey ,Enum as SQLEnum , UniqueConstraint
from database.connection import Base
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship 
from enum import Enum

class MonitorStatus(str,Enum):
    UP = "up"
    DOWN = "down"

class IncidentStatus(str,Enum):
    OPEN = "open"
    RESOLVED = "resolved"

class Monitor(Base):

    __tablename__ = "monitors"
    
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String(255),nullable=False)
    url = Column(String(2048),nullable=False)
    check_interval = Column(Integer,nullable=False)
    current_status = Column(SQLEnum(MonitorStatus),default=MonitorStatus.UP)
    is_active = Column(Boolean,default=True)
    last_checked_at = Column(DateTime(timezone=True))
    created_at = Column(DateTime(timezone=True),server_default = func.now())
    updated_at = Column(DateTime(timezone=True),server_default = func.now(),onupdate = func.now(),nullable=True)
    
    # Foreign Key
    user_id = Column(Integer,ForeignKey("users.id"),nullable=False)


    # Relationships
    user = relationship("User",back_populates="monitors")
    monitor_checks = relationship("MonitorCheck",back_populates="monitor",cascade="all, delete-orphan")
    incidents = relationship("Incident",back_populates="monitor",cascade="all, delete-orphan")

    # Constraint 

    __table_args__ = UniqueConstraint("user_id","url",name="unique_user_url")

class MonitorCheck(Base):

    __tablename__ = "monitor_checks"
    id = Column(Integer,primary_key=True,index=True)
    status = Column(SQLEnum(MonitorStatus),default=MonitorStatus.UP,nullable=False,index=True)
    status_code = Column(Integer)
    response_time_ms = Column(Integer,nullable=True)
    error_message = Column(String(500),nullable=True)
    created_at = Column(DateTime(timezone=True),server_default = func.now(),index=True)

    # Foreign Key
    monitor_id = Column(Integer,ForeignKey("monitors.id"),nullable=False,index=True)

    #RelationsShips and Foreign Key
    monitor = relationship("Monitor",back_populates="monitor_checks")

class Incident(Base):

    __tablename__ = "incidents"
    id = Column(Integer,primary_key=True,index=True)
    started_at = Column(DateTime(timezone=True),nullable=False)
    duration_in_seconds = Column(Integer)  # Duration for down time
    resolved_at = Column(DateTime(timezone=True),nullable=True)
    reason = Column(String(500),nullable=True)
    status = Column(SQLEnum(IncidentStatus),default=IncidentStatus.OPEN,nullable=False) # open/resolved
    created_at = Column(DateTime(timezone=True),server_default = func.now())

    # Foreign Key
    monitor_id = Column(Integer,ForeignKey("monitors.id"),nullable=False,index=True)

    # RelationsShips and Foreign Key
    monitor = relationship("Monitor",back_populates="incidents")

    









    
