from fastapi import APIRouter
from src.db import UserSchema, User, get_session, select
from typing import List

session = next(get_session())

user_router = APIRouter(
    prefix="/users",
    tags=["user"]
)

@user_router.get("/", response_model=List[UserSchema])
def get_all_users():
    return session.exec(select(User)).all()


@user_router.post("/", response_model=UserSchema)
def create_user(data: UserSchema):
    user_object = User(**data.model_dump())
    session.add(user_object)
    session.commit()
    session.refresh(user_object)
    return user_object

@user_router.get('/{username}', response_model=UserSchema)
def get_one_user(username: str):
    query = select(User).where(User.username == username)
    user = session.exec(query).first()

    if user:
        return user

    return {
        "mess": "Không tìm thấy"
    }
