from passlib.hash import argon2, bcrypt, sha256_crypt
from dotenv import load_dotenv
import jwt as jwt

import datetime

load_dotenv("./.env", override=True)

import os
SECRET_KEY = os.getenv('SECRET_KEY')

select_hash = bcrypt

if __name__ == "__main__":
    # password = "1231111111111111111111111111111111111111111111555555555555555"
    # hash_password = select_hash.hash(password)
    # print(hash_password.__len__())
    # print(hash_password)
    # print(select_hash.verify(password, hash_password))
    data_access = {
        'username': 'user0001',
        'password': '123',
        'phone': '123456789',
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=2),
        'type': 'ACCESS'
    }
    data_refresh = {
        'type': 'REFRESH',
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=10)
    }

    encrypt_data = jwt.encode(data_access, SECRET_KEY, 'HS256')

    print(encrypt_data)

    print(jwt.decode('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InVzZXIwMDAxIiwicGFzc3dvcmQiOiIxMjMiLCJwaG9uZSI6IjEyMzQ1Njc4OSIsImV4cCI6MTc1ODExNTUwM30.TJdigyOqUv9WyO8ujpVAfSGRcytNKy23j5XN9_1GevE', SECRET_KEY, ['HS256']))


    print(datetime.datetime.fromtimestamp(1758115503))
