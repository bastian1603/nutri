from app.models import User
from app.schemas import User as UserSchema
from app.db import session

from typing import Annotated
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm

import re

def create(user: UserSchema):
    if(user.password != user.password_confirmation):
        raise Exception("password dan konfirmasi password tidak sama")

    session.add(User(
        username=user.username, 
        email=user.email,
        password=user.password
    ))
    session.commit()

    return "Akun berhasil dibuat"

def destroy(id: int):
    try:

        user = session.query(User).filter(user.id == id).first()
        session.delete(user)

        return {
            "status": True,
            "message": "Your account deleted succesfully!"
        }

    except:
        return {
            "status": False,
            "message": "There is an error while deleting your eccount."
        }
    
def login(body: Annotated[UserSchema.Login, Depends()]):
    if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', body.identity) is not None:
        user = session.query(User).filter(User.email == body.identity).first()
    else :
        user = session.query(User).filter(User.username == body.identity).first()

    if not user:
        return {
            "status": False,
            "message": "Username atau Email yang anda masukkan salah."
        }

    if user.password == body.password:
        return {
            "status": True,
            "message": "Berhasil Login."
        }
    
    return {
        "status": False, 
        "message": "Password yang anda masukkan salah."
    }




def logout():
    pass