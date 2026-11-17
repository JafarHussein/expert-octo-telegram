from sqlalchemy import create_engine, text
from handlers.config import settings

engine=create_engine(settings.DATABASE_URL)

with engine.connect() as connection:
    result=connection.execute(text("SELECT 1"))