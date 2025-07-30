from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Engine = create_engine("sqlite:///../nutri.db", echo=False)
Base = declarative_base()
Session = sessionmaker(bind=Engine)
session = Session()