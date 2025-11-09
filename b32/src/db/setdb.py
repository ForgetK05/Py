from sqlmodel import (
    SQLModel,
    create_engine,
    Field,
    select,
    Session
)

from src.settings import DB_PATH
from typing import Optional

engine = create_engine(f"sqlite:///{DB_PATH}")


class AutoID(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)

class User(SQLModel):
    username: str = Field(unique=True, min_length=4, max_length=10)
    password: str = Field(min_length=4, max_length=500)


class UserDB(AutoID, User, table=True):
    ...


def create_all_talbes():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
    

from fastapi import Depends
from typing import Annotated

SessionDb = Annotated[Session, Depends(get_session)]
