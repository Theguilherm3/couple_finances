from sqlalchemy import inspect

from db.session import engine

inspector = inspect(engine)
print("Tabelas:", inspector.get_table_names())
