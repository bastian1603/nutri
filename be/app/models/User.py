from sqlalchemy import Column, String, Integer, Date, Float, Boolean
from sqlalchemy.orm import relationship, Mapped

from app.db import Base
from app.models.DailyConsumption import DailyConsumption

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    # birt_date = Column(Date, nullable=False)
    # weight = Column(Float, nullable=False)
    # height = Column(Float, nullable=False)

    daily_consumptions: Mapped[list["DailyConsumption"]] = relationship("DailyConsumption", back_populates="user")
    