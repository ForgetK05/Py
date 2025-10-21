from sqlmodel import (
    SQLModel,
    create_engine,
    select,
    Session,
    Field
)
from typing import *
from src.settings import DB_PATH

engine = create_engine(f"sqlite:///{DB_PATH}")

class AutoID(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)

class UserSchema(SQLModel):
    username: str = Field(min_length=5, max_length=10)
    password: str = Field(min_length=5, max_length=100)

class User(AutoID, UserSchema, table=True):
    ...

class AddressSchema(SQLModel):
    city: str
    street: str
    postcode: str

class Address(AutoID, AddressSchema, table=True):
    ...

class UserAddress(AutoID, table=True):
    user_id: int = Field(foreign_key=("user.id"))
    address_id: int = Field(foreign_key="address.id")

def create_all_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session

