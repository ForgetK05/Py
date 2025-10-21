# class Animal:
#     def __init__(self, name, weight):
#         self.name = name
#         self.weight=weight
    
#     def __str__(self):
#         return f'{self.name} {self.weight}'
    
#     def sound(self,):
#         ...
    

# class Dog(Animal):

#     def __init__(self, name, weight):
#         super().__init__(name, weight)
#         # Animal.__init__(self, name, weight)
#         # self.__init__(name, weight)
    
#     def sound(self,):
#         print('Gau')

# class Cat(Animal):

#     def __init__(self, name, weight):
#         super().__init__(name, weight)


#     def sound(self,):
#         print('Meo')


# dog = Dog('BUll', 100)
# dog.sound()

# meo = Cat('Katy', 30)
# meo.sound()

'''
Thiết kế các class quản lí phòng ban lập trình thì sẽ các vị trí:
- HR: người tuyển dụng
- BE: 
- FE:
- TESTER:
- MANAGER:
manager quản lí toàn bộ team be, fe, tester
hr liên hệ manager
'''

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} {self.age}'

class Manager(Person):
    def __init__(self, name, age, role='controls'):
        super().__init__(name, age)
        self.role=role

class HR(Person):
    def __init__(self, name, age, role='post-news'):
        super().__init__(name, age)
        self.role=role

class BE(Person):
    def __init__(self, name, age, tech_stack):
        super().__init__(name, age)
        self.tech_stack = tech_stack

    def __str__(self):
        return super().__str__()

class FE(Person):
    def __init__(self, name, age, tech_stack):
        super().__init__(name, age)
        self.tech_stack=tech_stack

    def __str__(self):
        return super().__str__()

class Tester(Person):
    def __init__(self, name, age, tech_stack):
        super().__init__(name, age)
        self.tech_stack = tech_stack

    def __str__(self):
        return super().__str__()


# in đầy đủ

# # Mới (sử dụng .join())
# class BE(Person):
#     # ... (các phần khác giữ nguyên)
#
#     def __str__(self):
#         # Nối các phần tử của list thành một chuỗi,
#         # dùng ', ' (phẩy và cách) làm ký tự phân cách.
#         tech_string = ', '.join(self.tech_stack)
#
#         return f'{super().__str__()} (BE - Tech: {tech_string})'
#
#
# class FE(Person):
#     # ... (các phần khác giữ nguyên)
#
#     def __str__(self):
#         tech_string = ', '.join(self.tech_stack)
#         return f'{super().__str__()} (FE - Tech: {tech_string})'
#
#
# class Tester(Person):
#     # ... (các phần khác giữ nguyên)
#
#     def __str__(self):
#         tech_string = ', '.join(self.tech_stack)
#         return f'{super().__str__()} (Tester - Tech: {tech_string})'

class TeamProject:
    def __init__(self, manager: Manager, members: list[BE|FE|Tester]):
        self.leader = manager
        self.members = members

    def __str__(self):
        return super().__str__()
    

class Contact:
    def __init__(self, owner, participant):
        self.owner = owner
        self.participant = participant


team_project = TeamProject(
    manager=Manager('Alice', 30,),
    members=[
        BE('Bob', 20, ['py', 'ai', 'fastapi']),
        FE('Katy', 22, ['react','js','ts','nvm'])
    ]
)

print(team_project.members[0])
print(team_project.members[1])