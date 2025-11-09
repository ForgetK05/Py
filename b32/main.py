from fastapi import FastAPI
from src.db.setdb import create_all_talbes
create_all_talbes()


app = FastAPI()

from src.routers.user import user_router


app.include_router(user_router)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", reload=True)