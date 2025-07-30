from typing import Union
from fastapi import FastAPI, Body, Request
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel

from app.db import Base, Engine
from app.models import User

Base.metadata.create_all(bind=Engine)


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # atau ["*"] untuk semua origin
    allow_credentials=True,
    allow_methods=["*"],  # Bisa diubah ke ['POST', 'GET'] jika mau dibatasi
    allow_headers=["*"],
)

@app.get('/')
def index():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id:int, q: Union[str, None] = None):
    return {
        "item_id": item_id, 
        "q" : q
    }

@app.post('/testing')
async def testing(username:str = Body(...)):
    try:
        return {'username': username}
    except Exception:
        return {'error': 'error'}
    