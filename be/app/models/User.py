from sqlalchemy import Column, String, Integer, Date, Float, Boolean
from sqlalchemy.orm import Relationship

from app.db import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    # birt_date = Column(Date, nullable=False)
    # weight = Column(Float, nullable=False)
    # height = Column(Float, nullable=False)