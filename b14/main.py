# try:
#     print(1/0)
# except Exception as error:
#     print(error)




# class Customer:

#     def __init__(self, name, age):
#         '''
#             private: "__" đặt trước tên thuộc tính/tên hàm thì sẽ không dùng được pham vi bên ngoài
#             public: truy cập ở bất kì vị nào
#             protected==public: _
#         '''
#         self.name = name
#         self.age = age
#         self.__hobbies = ["Music", "Tv"]
#         self._city = "TPHCM"

#     def payment(self, cost):
#         return cost *100-50
    
#     def hello(self):
#         print('hello')


# cus1 = Customer(name='Nam', age=30)
# print(cus1.name)
# print(cus1.age)
# # print(cus1.__hobbies)
# print(cus1._city)
# print(cus1.payment(cost=10))
# cus1.hello()


# class Person:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def __str__(self):
#         return f'{self.name}, {self.age}'
    



# person1 = Person(name='Nam', age=30)
# print(person1)


# class INT:

#     def __init__(self, n):
#         self.n = n
#     def __add__(self, other: 'INT'):
#         return INT(self.n + other.n)
#     def __str__(self):
#         return f'{self.n}'
    
# a = INT(1)
# b = INT(2)

# print(a+b)

'''
Các chức năng thuộc tính static: thường là các chức năng lặp đi lặp lại nhiều lần nên không cần sự khởi tạo để tránh lãng phí ô nhớ
'''

class Notice:
    APP_VERSION = '1.0.0'
    # vị trí đặt thuộc tính static

    @staticmethod
    def send_message(content):
        print(content)

Notice.send_message('Xin chào quí khách')
Notice.send_message('Xin chào quí khách')
Notice.send_message('Xin chào quí khách')
Notice.send_message('Xin chào quí khách')
Notice.send_message('Xin chào quí khách')
Notice.send_message('Xin chào quí khách')
Notice.send_message('Xin chào quí khách')

print(Notice.APP_VERSION)
print(Notice.APP_VERSION)
print(Notice.APP_VERSION)
print(Notice.APP_VERSION)
print(Notice.APP_VERSION)
print(Notice.APP_VERSION)
