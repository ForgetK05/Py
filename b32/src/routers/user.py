from fastapi import APIRouter
from src.db.setdb import SessionDb, UserDB, select, User

user_router = APIRouter(
    prefix="/users"
)


@user_router.get('/', response_model=list[User])
def get_all_users(session_db: SessionDb):
    query = select(UserDB)
    users = session_db.exec(query).all()

    return users


@user_router.post('/', response_model=User)
def create_one_user(data: User, session_db: SessionDb):
    user = UserDB(**data.model_dump())
