day_so = range(1, 10) # [a, b) => [1, 10) = 1->9

# for item in day_so:
#     print(item) # thực hiện đoạn code trong for


# for i in range(5):
#     for j in range(10):
#         print(f"i : {i}, j: {j}")

# for i in range(10):
#     print(i)
# else:
#     print("Lần lặp cuối cùng")


# dem = 0

# while dem < 10:
#     print(dem)
#     dem = dem + 1 # cứ qua 1 vòng lặp thì biến dem tăng thêm 1 đơn vị
# else:
#     print("Lần lặp cuối cùng")


"""
Các em dùng for khi biết trước số lượng, ngược lại không biết trước thì dùng while
"""

# Phần tích thừa số nguyên tố: 28 = 2*2*7 = 2^2 * 7^1
# n là số nguyên nhập từ bàn phím => biết trước range(n)
# n / 2->n kiểm tra xem có bao nhiêu thừa số => không biết trước tại vì sẽ chia cho tới khi không còn chia hết thì dừng lại => while

# Cách không tối ưu O(n)
# n = int(input())
# for i in range(2, n):
#     while n % i == 0:
#         print(i)
#         n = n // i # loại bỏ thửa số i vừa chia được ra khỏi n


# Cách tối ưu
# import math

# n = int(input()) # [a, b) b-1 O(căn n)
# for i in range(2, math.isqrt(n) + 1): # <= căn n
#     while n % i == 0:
#         print(i)
#         n = n // i # loại bỏ thửa số i vừa chia được ra khỏi n
#         # n bị chia cho i thì n giãm => for giãm

# if n > 1: # chưa hết 
#     print(n)

"""
01234:j,i , n = 5
***** 0 => j=4, i = 0
****  1 => j=4, i=1 => j 4 < n - i = 5 - 1 = 4
***   2
**    3
*     4
"""

# n = 5
# for i in range(n):
#     for j in range(n):
#         if j < n - i:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     # sau khi kết thúc for j => in xong 1 hàng
#     print() # in xuống hàng

import turtle
