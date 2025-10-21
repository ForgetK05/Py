# from abc import ABC, abstractmethod

# class Button(ABC):

#     def __init__(self, width, height):
#         self.widht = width
#         self.height = height

        
# class IButton(ABC):
#     @abstractmethod
#     def click(self): ...

#     @abstractmethod
#     def hover(self): ...

# class ZoomButton(
#     Button, 
#     IButton,
# ):

#     def __init__(self, width, height, zoom_val):
#         super().__init__(width, height)
#         self.zoom_val = zoom_val

#     def send(self,):
#         print('send')
    
#     def click(self,):
#         print('click ZoomButton')
    
#     def hover(self): ...


# but2 = ZoomButton(width=100, height=100, zoom_val=1.5)
# but2.click()



from dataclasses import dataclass

@dataclass
class User:
    username: str
    password: str

user_1 = User(username='user1', password='123')

print(user_1.username)
print(user_1.password)

from dataclasses import dataclass

@dataclass
class User:
    username: str
    password: str

    @dataclass
    class Meta:
        is_admin: bool

user = User(username='user1', password='123')
meta = user.Meta(is_admin=True)
user.meta=meta
print(user.meta.is_admin)

# a = [1, 4, 20, 2, 5]
# x = a[0]
# for i in a:
#       if i > x:
#             x = i
#       print(x)