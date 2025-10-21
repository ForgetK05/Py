import requests

# res = requests.get('http://127.0.0.1:8000/hello')
# print(res.json())


url = 'http://127.0.0.1:8000/users'

# Tạo 1 người dùng
res = requests.post(f"{url}", json={
    'username': 'user1',
    'password': '123'
})
print(res.json())
