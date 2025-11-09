from sqlmodel import (
    SQLModel,
    create_engine,
    Session,
    select,
    Field
)

from settings import DB_PATH
from typing import *
engine = create_engine(f"sqlite:///{DB_PATH}") # tạo file lưu dữ liệu

class User(SQLModel, table=True):
    id: Optional[str] = Field(default=None, primary_key=True)
    username: str = Field(unique=True)
    password: str = Field()


def create_all_table():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

