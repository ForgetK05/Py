from typing import TypeVar, Generic


T = TypeVar('T')

# class List(Generic[T]):
#     container = []

#     def push(self, value: T):
#         List.container.append(value)

#     def get_all_values(self) -> 'List[int]':
#         return List.container
    
# list_generic = List[int|float|str]()

# list_generic.push(100)
# list_generic.push(100)
# list_generic.push(100)

# print(list_generic.get_all_values())

# l = [1,2,3,4]

# for item in l:
#     print(id(item))


class Node(Generic[T]):

    def __init__(self, data: T, next_node = None):
        self.data = data
        self.next_node: 'Node' = next_node

class ListNode(Generic[T]): 

    first_node: Node[T] = None
    last_node: Node[T] = None

    def create_node(self, data: T):
        # Chưa có node nào hết
        new_node = Node[T](data)
        if ListNode.first_node == None:
            ListNode.first_node = new_node 
            ListNode.last_node = new_node
        # Đã có node
        else:
            ListNode.last_node.next_node = new_node
            ListNode.last_node = new_node

    def print_all_nodes(self, ):
        temp_node = ListNode.first_node
        
        while temp_node != None:
            print(temp_node.data)
            temp_node = temp_node.next_node

    def count_nodes(self, ):
        temp_node = ListNode.first_node
        dem = 0
        while temp_node != None:
            dem += 1
            temp_node = temp_node.next_node
        
        return dem

    def add_node(self, data: T, pos: int):

        # thêm vào đầu
        # thêm vào cuối
        # thêm vào giữa
        new_node = Node[T](data)
        if pos == 0:
            new_node.next_node = ListNode.first_node
            ListNode.first_node = new_node
    
            if ListNode.last_node == None:
                ListNode.last_node = new_node

        elif pos == self.count_nodes() - 1:
            if ListNode.first_node == None:
                ListNode.first_node = new_node
                ListNode.last_node = new_node
            else:
                ListNode.last_node.next_node = new_node
                ListNode.last_node = new_node

        
        else:
            front_node = ListNode.first_node
            back_node = front_node.next_node

            pos_dem = 0

            while front_node.next_node != None:
                if pos_dem == pos - 1:
                    break
                pos_dem += 1
                front_node = front_node.next_node
                back_node = front_node.next_node
        
            front_node.next_node = new_node
            new_node.next_node = back_node

# node1 = Node[int](100)
# node2 = Node[int](200)

# node1.next_node = node2

# print(id(node1))
# print(id(node1.next_node))
# print(node1.data)


list_node = ListNode[int]()

list_node.create_node(100)
list_node.create_node(200)
list_node.create_node(300)

list_node.add_node(400, 0)
list_node.add_node(1000, 1)
list_node.add_node(900, 3)

list_node.print_all_nodes()
