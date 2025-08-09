from fastapi import APIRouter, Depends, HTTPException, status
from typing import Annotated
from config import *


router = APIRouter()

# from fastapi import HTTPException, status
# from app.schemas.Token import Token
# from app.core.config import *
# import jwt
# from os import getenv
# from app.db import session
# from app.models import User

# class Route:

#     @staticmethod
#     def get(func, param: list | None = None):
#         status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
#         detail = "Internal Server Error."
#         try :
#             return func(*param)
#         except:
#             raise HTTPException(status_code=status_code,)


#     @staticmethod
#     def check_token(token: Token):
        
#         try:
#             payload = jwt.decode(token, key=JWT_SECRET_KEY, algorithms=JWT_ALGORITHM)
            
#             if Route.__check_user__(payload.get(id)) == None:
#                 raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found")
        
#             return True

#         except Exception as e:
#             detail = {
#                 "status_code": e.get("status_code", )
#             }    

#             raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")
        
#         except:
#             raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")
            
        

#     @staticmethod
#     def __check_user__(id: int):
#         user = session.query(User).filter(User.id == id).first()

#         return user


#     @staticmethod
#     def __error_handler__(e: dict | str):
#         if e.s