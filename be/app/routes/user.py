from app.routes.route import router
from app.db import session
from app.models import User
from app.schemas import User as UserSchema, Token as TokenSchema

from .auth import check_token 

@router.get("/")
def index():
    return {"hell9": "workd"}

@router.post("/get_profile")
def profile(body: TokenSchema.GetToken):
    user = check_token(body.access_token)
    
    return {
        "username": user.username,
        "email": user.email,
        "password": user.password
    }