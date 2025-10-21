# dem = 0 # global
# def count(): # bên trong hàm là phạm vi local
#     global dem # cấp quyền để truy cập ra ngoài phạm vi global từ local
#     dem += 1 # tăng giá trị biến đếm lên 1 đơn vị
#     dem1 = dem
#     print(dem+3)
#     def inner1():
#         nonlocal dem1
#         dem1 += 1
#         dem2 = dem1
#         print(dem1)

#         def inner2():
#             nonlocal dem2
#             dem2 += 1
#             print(dem2)
#         inner2()
#     inner1()
# count()



a, b, c = 0, 0, 0
def inner1(a=a):
    global b, c
    while b < 10: b += 1
    while a < 10: a += 1
    c += a+b
    res1=c
    def inner2(b=b):
        global a
        nonlocal res1
        _a = a # copy từ giá trị a sang _a
        while _a < 10:
            b += 1
            _a +=1
        res1 += b
        res2 = res1
        def inner3(a=a):
            nonlocal res2
            res3 = a*res2 
            print(res3)
        inner3()
    inner2()
inner1()
    
        
