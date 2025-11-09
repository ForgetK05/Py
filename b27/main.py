from src.routers import user_router
from fastapi import FastAPI
import uvicorn


app = FastAPI()

app.include_router(user_router)


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)


# /b27/
#     |
#     --- APIS, Routes: Định nghĩa các endpoint(đường link) cho ứng dụng
#     |
#     --- schemas: Lưu trữ các mô hình dữ liệu (data models) để khi request gửi tới ta có thể dễ dàng
#                       validate dữ liệu để kiểm tra tính hợp lệ của dữ liệu
#     |
#     --- database: Chứa các tập tin liên quan đến kết nối cơ sở dữ liệu và các thao tác với cơ sở dữ liệu
#     |
#     --- services: Chứa các tập tin liên quan đến logic nghiệp vụ của ứng dụng
#     |
#     --- settings.py: Chứa các tập tin cấu hình cho ứng dụng
#
# main.py: Tập tin chính để khởi động ứng dụng FastAPI