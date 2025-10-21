from sqlmodel import (
    SQLModel,
    Field,
    Session,
    create_engine,
    select
)

from settings import DB_PATH
from typing import *

engine = create_engine(f"sqlite:///{DB_PATH}")

class AutoID(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)

class User(SQLModel):
    username: str = Field(unique=True, min_length=5, max_length=10)
    password: str = Field(min_length=5, max_length=20)

class UserDB(AutoID, User, table=True):
    ...
    # ''''''
    # pass 

def create_all_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
    
