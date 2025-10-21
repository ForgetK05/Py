import requests

# res = requests.get("http://127.0.0.1:8000/users")
# print(res.json())

# res = requests.post("http://127.0.0.1:8000/users", json={
#     "username": "user00001",
#     "password": "12345"
# })
# print(res.json())


res = requests.get("http://127.0.0.1:8000/users/user00001")
print(res.json())