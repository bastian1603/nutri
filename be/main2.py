from typing import Union
from fastapi import FastAPI, Body, Query, Path, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel

from app.db import Base, Engine
# from app.models import User
from app.schemas import *
from app.controllers import *

# auth 
from datetime import datetime, timedelta
from jose import jwt, JWTError
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

SECRET_KEY = "a3f1c749b527e2b87c9c84f87fd645ad74dffdc93ae514fb6db30c8e05cf01b3"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

Base.metadata.create_all(bind=Engine)
app = FastAPI()

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
# oauth2_2_scheme = OAuth2PasswordBearer(tokenUrl="token")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # atau ["*"] untuk semua origin
    allow_credentials=True,
    allow_methods=["*"],  # Bisa diubah ke ['POST', 'GET'] jika mau dibatasi
    allow_headers=["*"],
)

# def verify_password(plain_password, hashed_password):
#     return pwd_context.verify(plain_password, hashed_password)

# def get_password_hash(password):
#     return pwd_context.hash(password)

# def get_user(db, username: str):
#     if username in db:
#         user_data = db[user_data]
#         return UserInDB(**user_data)

# def authenticate_user(db, username: str, password: str):
#     user = get_user(db, username)

#     if not user:
#         return False
#     if not verify_password(password, user.hashed_password):
#         return False
#     return user

# def create_access_token()