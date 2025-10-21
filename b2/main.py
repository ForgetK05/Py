# a = int(input())
# b = int(input())
# print(a+b)


# so_thuc = "2.5"

# print(int(float(so_thuc)))

# Chuỗi kí tự
# ngược nhau
# chuoi = ' I said "It is beautiful" '
# chuoi = " I said 'It is beautiful' "

# chuoi = '''
# ' I said "It is beautiful" '
# ' I said "It is beautiful" '
# ' I said "It is beautiful" '
# '''

# 3 cách print

# Cách 1:
# name = "Nguyen Van A"
# age = 21

# print("Tôi tên là: %s, tuổi : %.10f" % (name, age))


# Cách 2: dùng hàm chức năng format

# name = "Nguyen Van A"
# age = 21

# print("Tôi tên là: {}, tuổi là: {:.10f}".format(name, age))
# print()


# Cách 3: F-string

# name = "Nguyen Van A"
# age = 21

# print(f"Tên tôi là: {name}, tuổi là: {age}")
# print(f'Tên tôi là: {name}, tuổi là: {age}')


# menu = 121154

# # print(f"{menu:+^50}")
# # print(f"{menu:+>50}")
# # print(f"{menu:+<50}")

# print(f"{1:>10}")
# print(f"{12:>10}")
# print(f"{123:>10}")
# print(f"{1234:>10}")
# print(f"{12345:>10}")
# print(f"{123456:>10}")


# Xử lí chuỗi


# a = 1
# b = 1
# print(id(a))
# print(id(b))

# a = "1"
# b = "1"

# print(id(a))
# print(id(b))

# a = True
# b = True 
# print(id(a))
# print(id(b))

name = "        nGuyEn VaN CaO    "
print(name.strip().title())
print(name)
