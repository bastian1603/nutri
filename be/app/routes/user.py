from app.routes.route import router
from app.db import session
from app.models import User
from app.schemas import User as UserSchema, Token as TokenSchema

from .auth import check_token 
from fastapi import Depends
from config import *

@router.get("/")
def index():
    return {"hell9": "workd"}

@router.post("/get_profile")
def profile(token:str = Depends(oauth2_scheme)):

    
    user = check_token(token)

    
    
    return {
        "username": user.username,
        "email": user.email,
        "password": user.password
    }