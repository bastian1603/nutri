from sqlalchemy import Column, String, Integer, Date, Float, Boolean
from sqlalchemy.orm import relationship, Mapped

from app.db import Base
from app.models import DailyConsumption

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    # birth_date = Column(Date, nullable=True)
    # weight = Column(Float, nullable=True)
    # height = Column(Float, nullable=True)

    daily_consumptions: Mapped[list[DailyConsumption]] = relationship("DailyConsumption", back_populates="user", cascade="all, delete-orphan")
    