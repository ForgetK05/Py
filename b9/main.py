list_a = [1,2,3] + [1] * 10
list_b = [4,5,6]

# list_a.extend(list_b) # mở rộng giá trị cho list a sẽ được thêm giá trị từ list b vào cuối
# print(list_a + list_b)
# print(list_a)

list_a.insert(1, 1000)
# print(list_a)

# print(list_a.count(1))
# print(list_a.index(1))


# day_so = input().split()
# day_so_int = []
# for phan_tu in day_so:
#     day_so_int.append(int(phan_tu))

# print(day_so_int)

a = [1,2,3]
# b = a.copy()
# b.pop()
# print(a)

# copy_a = [*a] # *a -> 1,2,3 -> [....]
# print(id(a))
# print(id(copy_a))

# a.reverse() # thay đổi trực tiếp 
# copy_a = reversed(a) # không thay đổi ô nhớ trực tiếp
# print(list(copy_a))
# print(a)

# sort 

ds = [-20, 20, 1,2,3,5,3,2,10,1,4]

# tăng dương, giãm âm
def tieu_chi_1(item):
    if item % 2 == 0:
        return +item
    return -item

def tieu_chi_2(item):
    return (
        +abs(item), # độ ưu tiên đầu tiên là ưu tiên trị tuyệt đối
        -item, # độ ưu tiên số 2 sẽ được kích hoạt khi mà abs bằng nhau
    )


# ds.sort()
copy_ds = sorted(ds, key=tieu_chi_2)
# Tất built-in (hàm có sẵn) list đều thay đổi trực tiếp
print(ds)
print(copy_ds)
# tăng dần theo trị tuyết đối. abs(), nếu giá trị của trị tuyết đối bằng nhau thì kiểm tra so sánh giá ban đầu, ưu tiên tiên giá trị bé. |-20| == |20| => -20<20

# def h1():
#     return "Hello"

# def h2(h1=h1):
#     h1() # return "Hello"

# print(h2())


def Sort(ds=[], func=None):
    for item in ds:
        func(item)
        # xử lí logic 
    return ...