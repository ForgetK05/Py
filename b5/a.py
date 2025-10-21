"""
Cú pháp:
def tên_hàm(tham_số_1, tham_số_2, ...):
    # code triển khai
"""

# def hello():
    # print("Hello Của Module A")

# def tong(a, b):
#     return a + b # kết thúc và trả về giá trị sau return
#     # print("Hello")
#     # print("Hello")
#     # print("Hello")
#     # print("Hello")
#     # print("Hello")


# def tong(a=0, b=0):
#     return a + b


# print(tong(b=2))

# Thứ tự ưu tiên: bắc buộc trước sau đó là không bắc buộc


# def tong(a, b=0):
#     return a + b


# print()

# def tong(a: int, b: int):
#     ''' Docstring
#     # Đây là hàm tổng
#     ## Đây là hàm tổng
#     ### Đây là hàm tổng

#     Danh sách:
#         - phần tử 1
#         - phần tử 2

#     [Google](google.com)

#     **In đậm**
#     ___in ngiêng___
    
#     ![ddd]()
#     '''
#     return a + b


# def tong(a: int, b: int):
#     '''
#     Args:
#         - a: là số nguyên thứ nhất
#         - b: là số nguyên thứ hai

#     Returns:
#         - a + b: giá trị trả về
#     '''
#     return a + b


# print(tong())



from typing import Optional

# def tong(a: int | None = 0, b: int | None = 0):
#     return a + b


def tong(a: Optional[int] = 0, b: Optional[int] = 0):
    return a + b

print(tong())