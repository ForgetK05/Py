ds = [1,2,3,4]

# print([item**2 for item in ds if item % 2 == 0])

# def f(x):
#     if x % 2 == 0:
#         return x + 100
#     return x

# print(list(map(f, ds)))
# print(ds)


# Filter

# def f(x):
#     return x % 2 == 0
#
# print(list(filter(f, ds)))


# Reduce
from functools import reduce
def fx(x, y):
    return x + y

print(reduce(fx, ds, 0))


# ds = [1,2,3,4]
# tong = 0
# for item in ds:
#     tong = tong + item
# print(tong)

#
# ds_smartphone = [
#     # tên, giá, năm, model, color
#     # 0, 1, 2, 3, 4
#     ['Iphone 12 pro', 2000, 2021, 'apple', 'red'], # item[0]
#     ['Iphone 10 pro', 1500, 2023, 'apple', 'blue'],
#     ['Iphone 11 pro', 1800, 2021, 'apple', 'yellow'],
#     ['Samsung S20', 2500, 2022, 'samsung', 'red'],
#     ['Ipad 11', 2300, 2024, 'apple', 'red'],
#     ['Ipad 10', 1900, 2024, 'apple', 'red'],
#     ['Iphone 13 pro', 2500, 2021, 'apple', 'red'],
# ]

# tổng các sản phẩm năm 2021 của apple có màu đỏ
# Cách 1 dùng list comp
# loc_sp_2021 = [item[1] for item in ds_smartphone if item[2] == 2021 and item[3] == 'apple' and item[4] == 'red']


# loc_sp_2021 = list(map(lambda item: item[1], filter(lambda item: item[2] == 2021 and item[3] == 'apple' and item[4] == 'red', ds_smartphone)))
#
# print(sum(loc_sp_2021))


# tổng 3 sản có giá thấp nhât/ cao nhất

# tổng sản phẩm có giá <= 2000 của năm 2021

# tổng các sản phẩm apple trên 2000 của năm 2021