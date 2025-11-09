from fastapi import FastAPI
from db import (
    create_db_and_tables,
    get_session,
    get_user,
    create_user,
    delete_user,
    update_user,
    db_get_all_users,
    UserSchema
)
create_db_and_tables()
session = next(get_session())

app = FastAPI()

@app.get('/users/{username}') # 127.0.0.1:8000 + /hello
def get_one_user(username: str):
    return get_user(username=username, session=session)

@app.post('/users')
def create_one_user(data: UserSchema):
    return create_user(username=data.username, password=data.password, session=session)

@app.get('/users')
def get_all_users():
    return db_get_all_users(session=session)

@app.put('/users/{username}')
def update_one_user(username: str):
    return  update_user(username=username, new_password='new_password_123', session=session)

@app.delete('/users')
def delete_all_users():
    return delete_user(session=session)

@app.delete('/users/{username}')
def delete_one_users(username: str):
    return delete_user(username=username, session=session)


# 127.0.0.1:8000
if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', reload=True)