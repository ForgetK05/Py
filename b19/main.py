from typing import TypeVar, Generic

T = TypeVar('T')

from dataclasses import dataclass

@dataclass
class Product:
    price: float
    name: str
    color: str

class Node(Generic[T]):

    def __init__(self, data: T, front=None, back=None):
        self.front: 'Node' = front
        self.back: 'Node' = back
        self.data = data 
    

class DoubleLinkedList(Generic[T]):
    first: 'Node' = None
    last: 'Node' = None

    def create_node(self, data: T):
        new_node = Node[T](data=data)
        if DoubleLinkedList.first == None:
            DoubleLinkedList.first = new_node
            DoubleLinkedList.last = new_node
        else:
            DoubleLinkedList.last.back = new_node # gắn ô nhớ tiếp theo đi tới new_node
            new_node.front = DoubleLinkedList.last # new_node đi ngược về last cũ
            DoubleLinkedList.last = new_node   # cập nhật last cũ sang vị trí last mới

    def print_all_nodes(self, reverse=False):
        temp_node = DoubleLinkedList.first if reverse == False else DoubleLinkedList.last
        while temp_node != None:
            print(temp_node.data)
            temp_node = temp_node.back if reverse == False else temp_node.front


    def delete_node(self, pos: int):
        pos_dest = 0

        temp_node = DoubleLinkedList.first
        while temp_node != None:
            if pos_dest == pos:
                break
            pos_dest += 1
            temp_node = temp_node.back
        
        before_node = temp_node.front
        after_node = temp_node.back
        before_node.back = after_node
        after_node.front = before_node

    def count(self):
        dem = 0
        temp_node = DoubleLinkedList.first
        while temp_node != None:
            # print(temp_node.data)
            dem+=1
            temp_node = temp_node.back
        return dem

    def insert_node(self, data: T, pos):
        new_node = Node[T](data=data)
        if pos == 0:
            new_node.back = DoubleLinkedList.first
            DoubleLinkedList.first.front = new_node
            DoubleLinkedList.first = new_node
        elif pos == self.count() - 1:
            self.create_node(data)
        else:
            temp = DoubleLinkedList.first
            index = 0
            while temp != None and index < pos - 1:
                temp = temp.back
                index+=1
            new_node.back = temp.back
            temp.back=new_node
            new_node.front=temp
            new_node.back.front=new_node



    def update_node(self, data: T, pos):
        new_node = Node[T](data=data)
        if pos == 0:
            new_node.back = DoubleLinkedList.first
            DoubleLinkedList.first.front = new_node
            DoubleLinkedList.first = new_node
        elif pos == self.count() - 1:
            self.create_node(data)
        else:
            temp = DoubleLinkedList.first
            index = 0
            while temp != None and index < pos - 1:
                temp = temp.back
                index+=1
            new_node.back = temp.back
            temp.back=new_node
            new_node.front=temp
            new_node.back.front=new_node


dbll = DoubleLinkedList[Product]()

dbll.create_node(data=Product(price=30.5, name='ip14', color='red'))

map_prods = {}
map_prods['ip14'] = dbll



# double_ll = DoubleLinkedList[int]()
# double_ll.create_node(100)
# double_ll.create_node(200)
# double_ll.create_node(300)
# double_ll.create_node(400)

# # double_ll.delete_node(1)
# # double_ll.insert_node(500, 3)
# double_ll.update_node(1000, 1)
# double_ll.print_all_nodes()


# node1 = Node[int](100)
# node2 = Node[int](300)
# node3 = Node[int](200)

# ds = [node1, node2, node3]

# ds.sort(key=lambda item : item.data)

# for i in range(1, len(ds)):
#     ds[i].front = ds[i-1]
#     ds[i-1].back = ds[i]

# tmp = node1
# while tmp != None:
#     print(tmp.data)
#     tmp=tmp.back



