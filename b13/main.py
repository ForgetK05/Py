# se_1 = {1,2,3}
# list_1 = [1,2,3]

# print(1 in se_1) # O(1): luôn mất 1 thao tác
# print(1 in list_1) # O(n)

# ds = set(map(int, input().split()))

# print(ds)


# se_a = {1,2,3,4}
# se_b = {3,4,5,6}

# print(se_a.union(se_b)) # hàm chức union là của se_a sử dụng nên se_a sẽ bị biến đổi
# print(se_a | se_b) # toán tử hợp: 

# print(se_a - se_b) # phần có a nhưng không có phần b
# print(se_b - se_a) # phần có b nhưng không có phần a
# print(se_a & se_b) # phần mà a và b đều có
# print(se_a ^ se_b) # phần mà a và b đều có bỏ đi phần giao



# def tong(*args):
#     return 1,1,2,3


# print(tong(1,2,3,4,5))

# t = (1,2,3,4,5)
# # t[0]=0
# to_list = list(t)
# print(t)
# print(to_list)

# a,b,c = (1,2,3)
# a = 10
# print(a,b,c)

# so_nguyen: int = 0
# so_nguyen.

# from copy import deepcopy


# print(__file__)

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

INPUT_TEXT = BASE_DIR / "txt" / "in.txt"

'''
Read: đọc toàn bộ kí tự trong file -> str
Readlines: đọc từng hàng 1, list[str]
[
    "hello you\n",
    "hello you\n",
    "hello you\n",
    "hello you\n",
    "hello you",
]
'''
with open(INPUT_TEXT, mode="r", encoding="utf-8") as file:
    content = file.readlines()
    for hang in content:
        print(hang.replace("\n","")) # trong print đã có 1 lần xuống hàng mặc định rồi
