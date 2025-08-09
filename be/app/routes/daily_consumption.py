from app.routes.route import *
from app.routes.auth import check_token
from app.db import session
from app.routes import daily_consumption
from app.schemas import DailyConsumption as DayCompSchema
from app.models import DailyConsumption



@router.get("/")
async def index(keyword: str = "", token: str = Depends(oauth2_scheme)):
    user = check_token
    result = session.query(DailyConsumption).filter(DailyConsumption.user == user.id).get()

    return {
        status: True,
        result:result
    }

    # try:
    #     if keyword == "":
    #         result = result.get()
    #     else: 
    #         result = result.filter(DailyConsumption.food_name ==)

    # except:

@router.post("/")
async def create(body: DayCompSchema.createDailyConsumption, token = Depends(oauth2_scheme)):
    user = check_token(token)
    body.user_id = user.id

    session.add(DailyConsumption(
        food_name= body.food_name,
        calories= body.calories,
        user_id= body.user_id,
        datetime= body.datetime

    ))
    session.commit()

    return {
        "status": True,
        "message": "Berhasil menambahkan daily consumption"
    }


@router.patch("/")
async def update():
    pass


@router.delete("/")
async def delete():
    pass

