from app.models.model import *
from app.models import User

class WeightHistory(Base):
    __tablename__ = "weight_histories"
    id = Column(Integer, primary_key=True)
    weight = Column(Float, nullable=False)
    Date = Column(Date, nullable=False)
    user_id = Column(Integer, nullable=False)

    user: Mapped[User] = relationship("User", back_populates="weight_histories")
