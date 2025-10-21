from sqlmodel import (
    SQLModel,
    create_engine,
    select,
    Session,
    Field
)

engine = create_engine(f"sqlite:///./db.sqlite3")

class Book(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(min_length=5, max_length=500)


def create_all_talbes():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

from fastapi import Depends
from typing import Annotated

SessionDB = Annotated[Session, Depends(get_session)]
