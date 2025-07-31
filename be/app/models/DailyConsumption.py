from sqlalchemy import Column, String, Integer, Float, DateTime
from sqlalchemy.orm import Relationship

from app.db import Base

class DailyConsumption(Base):
    __tablename__ = "daily_consumptions"
    id = Column(Integer, primary_key=True)
    food_name = Column(String, nullable=False)
    calories = Column(Float, nullable=False)
    datetime = Column(DateTime, nullable=False)
