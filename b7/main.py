'''
tên_biến = lambda tham_số_1, tham_số_2, ...: biểu thức
tên_biến()
(lambda tham_số_1, tham_số_2, ...: biểu thức)()
ham()
'''

# print((lambda x, y: x+y)(1,2))

# tong = lambda x, y: x+y

# print(tong(1,2))

# if 1:   print(1);print(1);print(1)


ds = list(range(10))
# print(ds)

# for item in ds:
#     print(item)

# print(ds[0], ds[-len(ds)])
# print(ds[0], ds[-ds.__len__()])

# ds[0]=100
# print(ds)

# Append: dùng để thêm một phần tử vào cuối danh sách

# l = []
# l.append(1)
# l.append(2)
# print(l)

# n = int(input('Nhập số lượng phần tử: '))
# l = []
# while n:
#     l.append(int(input()))
#     n -= 1 # n sẽ bị trừ và giãm về 0. Lí do 0 là một giá trị luôn sai khi về 0 while sẽ dừng

# print(l)

# ds = input().split()

# for item in ds:
#     print(int(item)) # item sẽ bị thay đổi nhưng giá trị gốc của ds không bị. Vì giống như phép gán copy ra cho item

# print(ds)

# for vi_tri in range(len(ds)):
#     ds[vi_tri] = int(ds[vi_tri])

# print(ds)

ds = [
    1,
    2.0,
    3+2j,
    "Nguyen Van A",
    "Nguyen Van B"
]
ds_dap_an = []

# for item in ds:
#     if isinstance(item, str): # isinstance(giá trị, kiểu dữ liệu cần so sánh với gia trị)
#         ds_dap_an.append(item)
    
# print(ds_dap_an, ds)

# pop vs remove: xóa phần tử
# pop: mặc định nếu không có tham số thì xóa cuối, tham số phải là vị trí cần xóa
# remove: tham số là giá trị cần xóa

ds = [2,3,4] + [1]*5
# del ds[1]
# ds.pop()
# ds.remove(1)
# print(ds)

while (1 in ds): # nếu số 1 nằm cuối danh sách nó sẽ chạy tới cuối mời tìm thấy
    ds.remove(1)

print(ds)