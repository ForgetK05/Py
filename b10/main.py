# ds = [1,2,3,4,5]

# a, *b, c = ds

# print(a,b,c)

# new_ds = [*ds]

# print(new_ds)

# ds = [-10,-20,-5, 1, 2,20,10]

# def key(item):
#     return (
#         abs(item),
#         item if item % 2 == 0 else -item,
#     )

# new_ds = sorted(ds, key=key)

# print(new_ds)


'''
List Slicing
'''

ds = [5,2,3,6,4,7,5,9]
# new_ds = ds[:]
# print(id(new_ds))
# print(ds)
# print(id(ds))


# # Chèn 1 phần tử vào 1 vị trí bất kì: start == stop
# ds[1:1] = [1000]

# # Chèn vào đầu:
# ds[:0] = [5000]

# # Chèn vào cuối:
# ds[-1:] = [1000]

# print(ds)

# def sliding_window(ds, k):
#     '''
#     Args:
#         - ds: tập hợp các phần tử
#         - k: cụm các số liên tiếp được tính toán
#     '''
#     sums_of_wins = []
#     for item in range(0, len(ds)-k+1):
#         sums_of_wins.append(sum(ds[item: item+k]))
#     return max(sums_of_wins)

# print(sliding_window(ds, k=3))

ds[1:4]=[1,2,3] # thay thế trong 1 đoạn
ds[1:4]=[] # xóa trong 1 đoạn
ds[1:4] = sorted(ds[1:4]) # sắp xếp trong đoạn
print(ds)
