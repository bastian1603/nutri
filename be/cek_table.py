from sqlalchemy import inspect
from app.db import Engine, session
from app.models import *


inspector = inspect(Engine)

tables = inspector.get_table_names()

for table in tables:
    print(table)
    
    for column in inspector.get_columns(table):
        print(column['name'], column['type'])

    print("\n")

table = User
table_name = "users"

# Lihat kolom pada tabel tertentu
columns = inspector.get_columns(table_name)
for column in columns:
    print(column['name'], column['type'])


# lihat isi table
datas = session.query(User).all()

for data in datas:
    print(data.username, data.id, data.email, data.password)