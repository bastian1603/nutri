from sqlalchemy import Column, String, Integer, Float, DateTime
from sqlalchemy.orm import relationship, Mapped

from app.db import Base
from app.models.User import User

class DailyConsumption(Base):
    __tablename__ = "daily_consumptions"
    id = Column(Integer, primary_key=True)
    food_name = Column(String, nullable=False)
    calories = Column(Float, nullable=False)
    datetime = Column(DateTime, nullable=False)

    user: Mapped["User"] = relationship("User", back_populates="daily_consumptions", cascade="all, delete-orphan")

    def __repr__(self):
        return f"Address(id={self.id!r}, username={self.username!r})"