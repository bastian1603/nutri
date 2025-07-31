from pydantic import BaseModel
from datetime import datetime

class createDailyConsumption(BaseModel):
    food_name: str
    calories: float
    datetime: datetime
    