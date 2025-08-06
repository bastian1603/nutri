from app.db import session, Engine
from app.models import User
from sqlalchemy import delete

query = delete(User)
session.execute(query)

