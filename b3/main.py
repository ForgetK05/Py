# a, b = int(input()), int(input())

# if a > b:
#     print(f"Số a={a} lớn hơn số b={b}")
# else: # a <= b
#     print(f"{a} <= {b}")

# n= 0

# if n > 0:
#     print("N > 0")
# elif n > 0:
#     print("N > 0")
# elif n > 0:
#     print("N > 0")
# elif n > 0:
#     print("N > 0")
# elif n > 0:
#     print("N > 0")
# else: # n <= 0
#     print("N <= 0")
    
"""
Chia tiền: Số lượng n là giá trị của tờ tiền. Đổi n thành giá trị các tờ tiền sau: 5, 10, 20, 50, đổi ra giá trị ít nhất

Ví dụ: 205 = 4*50 + 5 => 5 tờ
"""

# n = int(input())

# so_to_tien_qui_doi, so_tien_du = 0, n

# if so_tien_du >= 50:
#     so_to_tien_qui_doi = so_to_tien_qui_doi + so_tien_du // 50 # cập nhật số tờ qui đổi được
#     so_tien_du = so_tien_du % 50 # cập tiền còn dư cho so_tien_du

# if so_tien_du >= 20:
#     so_to_tien_qui_doi = so_to_tien_qui_doi + so_tien_du // 20 # cập nhật số tờ qui đổi được
#     so_tien_du = so_tien_du % 20 # cập tiền còn dư cho so_tien_du

# if so_tien_du >= 10:
#     so_to_tien_qui_doi = so_to_tien_qui_doi + so_tien_du // 10 # cập nhật số tờ qui đổi được
#     so_tien_du = so_tien_du % 10 # cập tiền còn dư cho so_tien_du

# if so_tien_du >= 5:
#     so_to_tien_qui_doi = so_to_tien_qui_doi + so_tien_du // 5 # cập nhật số tờ qui đổi được
#     so_tien_du = so_tien_du % 5 # cập tiền còn dư cho so_tien_du

# print(so_to_tien_qui_doi)


# print(pow(2, 3, 1e9)) # 2 ^ 3 = 8 % 5 = 3


# if else trong 1 hàng => biểu thức => luôn trả về kết quả
# n = 10
# bieu_thuc = n * 100 if n > 0 else n / 100
# print(bieu_thuc)