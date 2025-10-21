from fastapi import APIRouter
from src.db import (
    UserDB,
    User,
    select,
    get_session
)
from typing import *

user_router = APIRouter(
    prefix="/users",
    tags=["user"]
)

session = next(get_session())

@user_router.get('/', response_model=List[User])
def get_all_users():
    query = select(UserDB)
    users = session.exec(query).all()

    return users


@user_router.post('/', response_model=User)
def create_user(data: User):
    user = UserDB(
        **data.model_dump()
    )

    session.add(user)
    session.commit()
    session.refresh(user)

    return user

