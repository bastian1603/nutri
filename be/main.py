from typing import Union, Annotated
from fastapi import FastAPI, Body, Query, Path, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel

from app.db import Base, Engine
# from app.models import User
# from app.schemas import *
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

@app.post('/testing')
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
    

@app.get('/a')
async def check():
    return {
        'a': session.query()
    }

# @app.post('/testing')
# async def testing(username:str = Body(...)):
#     try:
#         return {'username': username}
#     except Exception:
#         return {'error': 'error'}
    

class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None

def decode_token(token):
    return User (
        username= token + "fakedecoded", email="john@example", full_name = "John Doe"
    )

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = decode_token(token)
    return user