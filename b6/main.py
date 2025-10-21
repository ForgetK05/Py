# n = int(input())

# match n:
#     case 1:
#         print("31")
#     case 2:
#         print("N = 2")
#     case 3:
#         print("31")
#     case _:
#         print("Mặc định khi mà không có trường hợp nào khớp")


# def tong(*args):
#     sum=0
#     for item in args:
#         sum+=item
#     return sum

# tong(1,2,3,4,5)

# chuoi = "Hello"
# for item in chuoi:
#     print(item)

# day_so = range(10)


def tong(*args):
    return sum(args)

# a = tong # chưa chạy gọi là truyền hàm
# # a = tong() # đã chạy gọi là truyền kết quả đầu ra của hàm

# print(a(1,2,3,4))

# def call_tong(*args, fn=tong):
#     return fn(*args)

# print(call_tong(1,2,3,4,5))



# def tong(sum=0):
#     for item in range(10):
#         sum+=item
#     return sum

# print(tong()) # đáp án?

# def a(*args, t=1):
#     for item in args:
#         t *= item
#     return t

# def b(fn_a=a, ch='a'):
#     return fn_a(1,2,3)*ch

# def c(fn_b=b, cnt=0):
#     for item in fn_b():
#         cnt+=1
#     return cnt

# print(c()) # c?


def tong(a: int, b: int):
    return a + b

# Truyền hàm chú thích?

from typing import Callable

TongType = Callable[
    [int, int], # chỗ trống đầu tiên là kiểu dữ liệu của tham số
    int # kiểu dữ liệu đầu ra
]

def call_tong(*args, fn: TongType = tong):
    return fn(*args)