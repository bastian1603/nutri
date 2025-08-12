from pydantic import BaseModel
from datetime import datetime

class createDailyConsumption(BaseModel):
    food_name: str
    calories: float
    # datetime: str | None = None
    user_id: int | None = None

class update_DailyConsumption(BaseModel):
    food_name: str = "asasa"
    calories: float = 1.9
    