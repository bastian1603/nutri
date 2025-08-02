from typing import Union, Annotated
from fastapi import FastAPI, Body, Query, Path, HTTPException, Depends, Form
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel
import re

from app.db import Base, Engine
# from app.models import User
from app.schemas import *
from app.controllers import *

# auth 
# from datetime import datetime, timedelta
# from jose import jwt, JWTError
# from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

# SECRET_KEY = "a3f1c749b527e2b87c9c84f87fd645ad74dffdc93ae514fb6db30c8e05cf01b3"
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 30

Base.metadata.create_all(bind=Engine)
app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# fake_db = {
#     "tim": {
#         "username": "tim",
#         "full_name": "Tim Rusica",
#         "email": "tim@gmail.com",
#         "hashed_password": "",
#         "disabled": False
#     }
# }

# class Token(BaseModel):
#     access_token: str
#     token_type: str

# class TokenData(BaseModel):
#     username:str | None = None

# class User(BaseModel):
#     username: str
#     full_name: str | None = None
#     email: str | None = None
#     disabled: bool | None = None

# class UserInDB(User):
#     hashed_password:str

# pwd_context = CryptContext(schemes=["bcrypt", depreacted="auto"])


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # atau ["*"] untuk semua origin
    allow_credentials=True,
    allow_methods=["*"],  # Bisa diubah ke ['POST', 'GET'] jika mau dibatasi
    allow_headers=["*"],
)

# def verify_password():
    

@app.get('/')
def index():
    return {"Hello": "World"}

@app.get("/items")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}

@app.get("/items/{item_id}")
def read_item(item_id:int = 10, q: Union[str, None] = None):
    return {
        "item_id": item_id, 
        "q" : q
    }

@app.post('/register')
async def testing(body: CreateUser):
    try :
        result = UserController.create(body)

        return {
            "status": True, 
            "message" : result
        }
    except Exception as e: 
        return {
            "status": False,
            "error": str(e),
        }
    
    
def LoginForm(body):
    formatted_body: Login
    try:
        formatted_body = Login(body)
        formatted_body.use_email = True

    except:
        formatted_body.use_email = False

    
    return formatted_body


@app.post('/token')
async def login(body: Login):
    result = UserController.login(body)
    
    # valid = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', body.identity) is not None

    
    # return {
    #     "identity": body.identity,
    #     "valid": valid
    #     # "is_email_str": is_email_str,
    #     # "actual_type": actual_type
    # }

    return result


@app.get('/a')
async def check():
    return {
        'a': session.query()
    }