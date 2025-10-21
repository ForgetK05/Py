from src.routers.user import user_router
from fastapi import FastAPI
from src.db import create_all_tables

create_all_tables()

app = FastAPI()

app.include_router(router=user_router)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", reload=True)