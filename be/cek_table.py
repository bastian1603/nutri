from sqlalchemy import inspect
from app.db import Engine

inspector = inspect(Engine)

tables = inspector.get_table_names()

for table in tables:
    print(table)
    
    for column in inspector.get_columns(table):
        print(column['name'], column['type'])

    print("\n")

# # Lihat kolom pada tabel tertentu
# columns = inspector.get_columns('daily_consumption')
# for column in columns:
#     print(column['name'], column['type'])