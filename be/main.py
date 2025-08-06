from typing import Union, Annotated
from fastapi import FastAPI, Body, Query, Path, HTTPException, Depends, Form
from fastapi.middleware.cors import CORSMiddleware
from handlers.service import Handlers

from pydantic import BaseModel
# import re

from app.db import Base, Engine
# from app.models import User
from app.schemas import *
from app.controllers import *

# auth 
# from datetime import datetime, timedelta
# from jose import jwt, JWTError
# from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt
from jwt.exceptions import InvalidTokenError
import os
from dotenv import load_dotenv


load_dotenv("./.env")
Base.metadata.create_all(bind=Engine)
app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



SECRET_KEY = os.getenv("JWT_SECRET_KEY")
ALGORITHM = os.getenv("JWT_ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("JWT_ACCESS_TOKEN_EXPIRE_MINUTES")

@app.get('/')
def index():
    return {"Hello": SECRET_KEY}

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