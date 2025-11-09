from fastapi import FastAPI
from db import create_all_table, select, User, get_session

create_all_table()

session = next(get_session())
app = FastAPI()



@app.get("/users")
def get_all_users():
    users = session.exec(select(User))

    return [
        user.model_dump()
        for user in users
    ]


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", reload=True)