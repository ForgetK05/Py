# # from passlib.hash import sha256_crypt
# from passlib.hash import argon2,bcrypt
# bcrypt.__about__.__version__='5.0.0'
# select_hash = bcrypt
#
# if __name__ == '__main__':
#     password = '1234526'
#     # hashed_password = sha256_crypt.hash(password)
#     # print(f"Hashed password: {hashed_password}")
#     # # Độ dài của chuỗi băm không thay đổi dù mật khẩu có dài hay ngắn
#     # # Cố định độ dài chuỗi băm và tốc độ
#     # print(len(hashed_password))
#
#     hashed_password = select_hash.hash(password)
#     print(f"Hashed password: {hashed_password}")
#     # Độ dài của chuỗi băm không thay đổi dù mật khẩu có dài hay ngắn
#     # Cố định độ dài chuỗi băm và tốc độ
#     print(len(hashed_password))

# from dotenv import load_dotenv
# load_dotenv('.env', override=True)
# import os
# SECRET_KEY = os.getenv('SECRET_KEY')
#
# if __name__ == '__main__':
#     print(f"SECRET_KEY: {SECRET_KEY}")

