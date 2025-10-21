from fastapi import APIRouter

user_router = APIRouter(
    prefix='/users'
)

@user_router.get('/') # http://127.0.0.1:800/users/
def get_all_users():
    return {
        'data': 'Get All Users Request'
    }