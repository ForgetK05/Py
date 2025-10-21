from fastapi import FastAPI
from db import (
    create_db_and_tables,
    get_session,
    get_user,
    create_user,
    delete_user,
    update_user,
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
    ...

@app.put('/users/{username}')
def update_one_user(username: str):
    ...

@app.delete('/users')
def delete_all_users():
    ...

@app.delete('/users/{username}')
def delete_one_users(username: str):
    ...


# 127.0.0.1:8000
if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', reload=True)