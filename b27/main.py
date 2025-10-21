from src.routers import user_router
from fastapi import FastAPI
import uvicorn


app = FastAPI()

app.include_router(user_router)


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)