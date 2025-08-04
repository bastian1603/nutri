from app.models import User
from app.schemas import User as UserSchema
from app.db import session

from typing import Annotated
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm

from passlib.context import CryptContext
import jwt 
import re

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserController:
    
    @staticmethod
    def create(user: UserSchema):
        if(user.password != user.password_confirmation):
            raise Exception("password dan konfirmasi password tidak sama")

        session.add(User(
            username=user.username, 
            email=user.email,
            password= pwd_context.hash(user.password)
        ))
        session.commit()

        return "Akun berhasil dibuat"
    

    @staticmethod
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
        

    @staticmethod    
    def login(body: Annotated[UserSchema.Login, Depends()]):
        try:

                
            if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', body.identity) is not None:
                user = session.query(User).filter(User.email == body.identity).first()
            else :
                user = session.query(User).filter(User.username == body.identity).first()

            if not user:
                return {
                    "status": False,
                    "message": "Username atau Email yang anda masukkan salah."
                }

            if pwd_context.verify(body.password, user.password):
                return {
                    "status": True,
                    "message": "Berhasil Login."
                }
            
            return {
                "status": False, 
                "message": "Password yang anda masukkan salah."
            }
        except Exception as e:
            return {
                "status": False,
                "message": str(e)
            }

    @staticmethod
    def logout():
        pass