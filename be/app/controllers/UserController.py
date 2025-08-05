from app.models import User
from app.schemas import User as UserSchema
from app.db import session

from typing import Annotated
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from passlib.context import CryptContext
import jwt 
import re
from functools import wraps

def handler(func):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

    try: 
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result
        
        return wrapper

    except:
        raise HTTPException(status_code=status_code)




from app.controllers.TokenController import TokenController


class UserController:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    
    @staticmethod
    def create(user: UserSchema):
        if(user.password != user.password_confirmation):
            raise Exception("password dan konfirmasi password tidak sama")

        session.add(User(
            username=user.username, 
            email=user.email,
            password= UserController.pwd_context.hash(user.password)
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
        status_code
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

            if not UserController.pwd_context.verify(body.password, user.password):
                return {
                    "status": False, 
                    "message": "Password yang anda masukkan salah."
                }


            data = {
                "username": user.username,
                "email": user.email,
                "id": user.id
            }
            token = TokenController.create_access_token(data)

            return {
                "status": True,
                "message": "Berhasil Login.",
                "token": token
            }
            
        except Exception as e:
            if status_code == None:
                status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

            raise HTTPException(
                status_code=status_code,
                detail= {
                    "status": False,
                    "message": str(e)
                }
            )

    @staticmethod
    def logout():
        pass


    @staticmethod
    def get_user(id: int | None = None):
        status_code = None

        try:
            user = session.query(User).filter(User.id == id).first();
            if not user:
                status_code = status.HTTP_401_UNAUTHORIZED

                raise Exception("Gagal memvalidasi user")

            return user
        except Exception as e:
            if status_code == None:
                status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

            raise HTTPException(
                status_code=status_code,
                detail= {
                    "status": False,
                    "message": str(e)
                }
            )