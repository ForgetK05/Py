from typing import TypeVar, Generic,Generator


T = TypeVar('T')

class List(Generator[T]):
    container = []

    def add(self, value: T):
        List.container.append(value)


lst = List[float]()

lst.add(2)

#
# class Model(Generator[T]):
#
#     def __init__(self, obj: T):
#         self.obj = obj
#
#
# class Admin:
#     ...
#
# model_user = Model[Admin]()
#
# T = TypeVar('T')
#
# class Stack(Generic[T]):
#
#     container = []
#
#     def push(self, value: T):
#         Stack.container.append(value)
#
#     def pop(self):
#         Stack.container.pop()
#
#     def get_values(self) -> 'Stack[int]':
#         return Stack.container
#
# stack_int = Stack[int]()
#
# stack_int.push(1)
# stack_int.push(5)
# stack_int.push(3)
#
# print(stack_int.get_values())


# class User:
#     ...

# stack_user = Stack[User]()


# T = TypeVar('T')

# class Node(Generic[T]):

#     def __init__(self, data: T = None, next_node = None):
#         self.current_node = self
#         self.data = data
#         self.next_node: 'Node' = next_node

# class Nodes(Generic[T]):
#     first_node: Node[T] = None
#     last_node: Node[T] = None

#     def create(self, data: T):
#         Nodes.first_node = Node[T](data)
#         Nodes.last_node = Nodes.first_node
#         return Nodes.first_node

#     def add(self, node: Node[T]):
#         if not Nodes.first_node:
#             return
#         Nodes.last_node.next_node = node
#         Nodes.last_node = node

# manage_nodes = Nodes[int]()

# manage_nodes.create(100)
# manage_nodes.add(Node[int](200))

# print(manage_nodes.first_node.data)
# print(manage_nodes.first_node.next_node.data)
# print(manage_nodes.last_node.data)


# T = TypeVar('T')
#
# class Node(Generic[T]):
#
#     def __init__(self, data: T = None, next_node = None):
#         self.before_node: 'Node' = None
#         self.data = data
#         self.next_node: 'Node' = next_node
#
# class Nodes(Generic[T]):
#     first_node: Node[T] = None
#     last_node: Node[T] = None
#
#     def create(self, data: T):
#         Nodes.first_node = Node[T](data)
#         Nodes.last_node = Nodes.first_node
#         return Nodes.first_node
#
#     def add(self, node: Node[T]):
#         if not Nodes.first_node:
#             return
#         Nodes.last_node.next_node = node
#         node.before_node = Nodes.last_node
#         Nodes.last_node = node
#
#     def remove(self, value: T):
#         if value == Nodes.first_node.data:
#             if not Nodes.first_node.next_node:
#                 Nodes.first_node = None
#                 Nodes.last_node = None
#             else:
#                 next_node = Nodes.first_node.next_node
#                 Nodes.first_node.next_node = None
#                 Nodes.first_node = next_node
#                 Nodes.first_node.before_node = None
#
#         if value == Nodes.last_node.data:
#             if not Nodes.first_node.next_node:
#                 Nodes.first_node = None
#                 Nodes.last_node = None
#             else:
#                 before_node = Nodes.last_node.before_node
#                 Nodes.last_node.before_node = None
#                 Nodes.last_node = before_node
#                 Nodes.last_node.next_node = None
#
#         temp_node = Nodes.first_node
#
#         while temp_node.next_node != None:
#             if value == temp_node.data:
#                 be_node = temp_node.before_node
#                 af_node = temp_node.next_node
#                 be_node.next_node = af_node
#                 af_node.before_node = be_node
#
#             temp_node = temp_node.next_node
#
#
#
# manage_nodes = Nodes[int]()
# manage_nodes.create(100)
# manage_nodes.add(Node[int](200))
# manage_nodes.add(Node[int](300))
#
# manage_nodes.remove(200)
#
# print(manage_nodes.first_node.next_node.data)
        






