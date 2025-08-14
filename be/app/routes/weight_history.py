from app.routes.route import *
from app.models import WeightHistory
from .auth import check_token

@router.get("/")
def index(token: oauth2_scheme):
    user = check_token(token)

    result = user.weight_histories()


@router.post("/")
def create(body, token: oauth2_scheme):
    pass


@router.put("/{id}")
def update(id: int, token: oauth2_scheme):
    pass


@router.delete("/{id}")
def destroy(id:int, token: oauth2_scheme):
    pass