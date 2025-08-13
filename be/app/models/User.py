from app.models.model import *
from app.models import DailyConsumption, WeightHistory

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
    weight_histories: Mapped[list[WeightHistory]] = relationship("WeightHistory", back_populates="user", cascade="all, delete-orphan")