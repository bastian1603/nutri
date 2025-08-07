from os import getenv
from dotenv import load_dotenv
from fastapi.security import OAuth2PasswordBearer

load_dotenv()

JWT_SECRET_KEY = getenv("JWT_SECRET_KEY")
JWT_ALGORITHM = getenv("JWT_ALGORITHM")
JWT_ACCESS_TOKEN_EXPIRE_MINUTES = int(getenv("JWT_ACCESS_TOKEN_EXPIRE_MINUTES"))

TOKEN_URL = getenv("TOKEN_URL")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl=TOKEN_URL)