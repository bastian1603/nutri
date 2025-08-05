import jwt
from jwt.exceptions import InvalidTokenError
from datetime import timedelta, datetime

from os import getenv
from app.schemas import Token


class TokenController():
    algorithm = getenv("JWT_ALGORITHM")
    secret_key = getenv("JWT_ALGORITHM")
    access_token_expire_minutes=getenv("JWT_ACCESS_TOKEN_EXPIRE")

    @staticmethod
    def create_access_token(user: dict, expires_delta: timedelta | None = None):
        to_encode = {
            "sub": user["username"],
            "email": user["email"] 
        }

        if expires_delta:
            expire = datetime.now() + expires_delta
        else:
            expire = datetime.now() + timedelta(minutes=30)
        
        to_encode.update({"exp" : expire})
        encoded_jwt = jwt.encode(to_encode, key=TokenController.secret_key, algorithm=TokenController.algorithm)

        return encoded_jwt
    
    @staticmethod
    def token_validation(token: Token):
        payload = jwt.decode(token, key=TokenController.secret_key, algorithms=[TokenController.algorithm])
