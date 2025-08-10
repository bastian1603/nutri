from app.routes.route import *
from app.routes.auth import check_token
from app.db import session
from app.routes import daily_consumption
from app.schemas import DailyConsumption as DayCompSchema
from app.models import DailyConsumption



@router.get("/")
async def index(keyword: str = "", token: str = Depends(oauth2_scheme)):
    user = check_token(token)
    result = session.query(DailyConsumption).filter(DailyConsumption.user_id == user.id).all()

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
        datetime= body.datetime
    ))
    session.commit()

    return {
        "status": True,
        "message": "Berhasil menambahkan daily consumption"
    }


@router.patch("/{id}")
async def update(id: int, body: DayCompSchema.createDailyConsumption, token=Depends(oauth2_scheme)):
    user = check_token(token)
    item = session.query(DailyConsumption).filter(DailyConsumption.id == id).first()

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

