from fastapi import Form
from pydantic import BaseModel, EmailStr

class CreateUser(BaseModel):
    username: str
    email: EmailStr
    password: str
    password_confirmation: str

class Login(BaseModel):
    identity: EmailStr | str
    password: str