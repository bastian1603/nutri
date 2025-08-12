from .route import *
from fastapi.security import OAuth2PasswordBearer
from datetime import timedelta, datetime

from config import *
import jwt
from passlib.context import CryptContext
from pydantic import EmailStr 

from app.db import session
from app.models import User
from app.schemas import User as UserSchema
from re import match
from sqlalchemy import or_


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

# @router.get("/")
# async def testing():
#     return {"hello": "world"}

@router.post("/register")
def register(user: UserSchema.CreateUser):
    try:
        user_exists = session.query(User).filter(or_(User.username == user.username, User.email == user.email)).first()

        if user_exists:
            e = {}

            if user_exists.username == user.username:
                e.update({"username": 1})
            if user_exists.email == user.email:
                e.update({"email": 1})

            raise Exception(e)            
            # if user_exists.username == user.username and user_exists.email == user.email:
                
            #     raise Exception("Username dan Email sudah digunakan")
            # elif user_exists.username == user.username:
            #     raise Exception("Username sudah digunakan")
            # else:
            #     raise Exception("Email sudah digunakan")

        if(user.password != user.password_confirmation):
            raise Exception("password dan konfirmasi password tidak sesuai")
        
        hashed = pwd_context.hash(user.password)

        session.add(User(
            username=user.username,
            email=user.email,
            password=hashed
        ))
        session.commit()
        
        return {
            "status": True,
            "message": "Akun berhasil dibuat"
        }

    except Exception as e:
        (arg, ) = e.args
        
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail={
            "username": str(arg["username"]),
            "email": str(arg["email"])
        })
    

@router.post("/login")
def login(input: UserSchema.Login):

    try:
        if match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', input.identifier) is not None:
            user = session.query(User).filter(User.email == input.identifier).first()       
        else:
            user = session.query(User).filter(User.username == input.identifier).first()

        if not user:
            raise Exception("User dengan username atau email tersebut tidak ditemukan")

        if not pwd_context.verify(input.password, user.password):
            raise Exception("Password yang anda berikan salah!")
        
        user_data= {
            "sub": user.username,
            "email": user.email,
            "id": user.id
        }
        token = __create_token(user_data)

        return {
            "status": True,
            "token": token,
            "message": "Berhasil Login"
        }
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))   


def __create_token(to_encode: dict, expires_delta: timedelta | None = None):

    if not expires_delta == None:
        expires = datetime.now() + expires_delta
    else:
        expires = datetime.now() + timedelta(minutes=JWT_ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode.update({"exp": int(expires.timestamp())})

    jwt_encoded = jwt.encode(to_encode, key=JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
    return jwt_encoded

        
def check_token(token):
    try:
        
        payload =  jwt.decode(token, key=JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])

        user = session.query(User).filter(User.id == payload.get("id")).first()

        if not user:
            raise Exception("Token tidak valid")
        
        return user
    
    except Exception as e:
        raise  HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))
    

    

