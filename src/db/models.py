# This is where we going to write python code that is going to be translated into an postgresql queries using the ORM

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Integer, Boolean

class Base(DeclarativeBase):
    pass

