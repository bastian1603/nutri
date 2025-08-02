from app.models import User
from app.schemas import User as UserSchema
from app.db import session

from typing import Annotated
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm

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
    
def login(form: Annotated[UserSchema.Login, Depends()]):
    user:str
    if isinstance(form.identity, str):
        user = session.query(User).filter(User.username == form.identity).first()
    else :
        user = session.query(User).filter(User.email == form.identity).first()

    if not user:
        return {
            "status": False,
            "message": "Username atau Email yang anda masukkan salah."
        }

    if user.password == form.password:
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