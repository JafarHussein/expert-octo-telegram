# This is where we are going to make the connection with the database and establish a connection

from sqlalchemy import create_engine, text
from .config import settings

engine=create_engine(settings.DATABASE_URL)

with engine.connect() as connection:
    result=connection.execute(text("SELECT 1"))
    
    print(result.scalar())