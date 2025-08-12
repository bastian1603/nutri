from app.routes.route import *
from app.routes.auth import check_token
from app.db import session
from app.routes import daily_consumption
from app.schemas import DailyConsumption as DayCompSchema
from app.models import DailyConsumption
from datetime import datetime, timedelta


@router.get("/{time}")
async def index(time: int = 0, token: str = Depends(oauth2_scheme)):
    time /= 1000
    user = check_token(token)
    day1 = datetime.fromtimestamp(time)
    day2 = datetime.fromtimestamp(time + 86400)
    day1 = str(day1)
    day2 = str(day2)

    result = session.query(DailyConsumption).filter(DailyConsumption.user_id == user.id).filter(DailyConsumption.datetime >= day1).filter(DailyConsumption.datetime < day2).all()

    a = None

    # if result:
    #     a = result.calories

    return {
        "status": True,
        "results": result
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
        datetime= datetime.now()
    ))
    session.commit()

    return {
        "status": True,
        "message": "Berhasil menambahkan daily consumption"
    }


@router.put("/{id}")
async def update(id: int, body:DayCompSchema.update_DailyConsumption, token=Depends(oauth2_scheme)):

    user = check_token(token)
    item = user.daily_consumptions.filter(DailyConsumption.id == id).first()

    item.food_name = body.food_name
    item.calories = body.calories

    session.commit()

    return {
        "status": True,
        "message": "Berhasil Diedit"
    }


@router.delete("/{id}")
async def delete(id: int, token=Depends(oauth2_scheme)):
    user = check_token(token)
    item = session.query(DailyConsumption).filter(DailyConsumption.id == id).first()
    session.delete(item)
    session.commit()

    return {
        "status": True,
        "message": "Berhasil Dihapus"
    }

