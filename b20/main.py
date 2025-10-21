from typing import Generic, TypeVar, Optional
from dataclasses import dataclass

TemplateStack = TypeVar('TemplateStack')



class Node(Generic[TemplateStack]):

    def __init__(self, data: Optional[TemplateStack] = None, next_node: Optional['Node'] = None):
        self.data: TemplateStack = data
        self.next_node = next_node

class Stack(Generic[TemplateStack]):
    top_stack : Optional['Node'] = None

    def push(self, data: TemplateStack):
        new_node = Node[TemplateStack](data=data)

        if Stack.top_stack == None:
            Stack.top_stack = new_node

        else:
            new_node.next_node = Stack.top_stack
            Stack.top_stack = new_node

    def pop(self,):
        current_top_stack = Stack.top_stack
        Stack.top_stack = Stack.top_stack.next_node
        current_top_stack.next_node = None

        return current_top_stack.data


    def list_all(self):
        temp = Stack.top_stack

        while temp != None:
            print(temp.data)
            temp = temp.next_node
        
    def count(self):
        temp = Stack.top_stack
        dem = 0
        while temp != None:
            dem += 1
            temp = temp.next_node
        return dem


# stack = Stack[int]()
# stack.push(100)
# stack.push(200)
# stack.push(300)
# print('Stack đã xóa', stack.pop())

# stack.list_all()

# (())

# stack = Stack[str]()
# expression = input()

# for char in expression:
#     if char == ')' or char == '(':
#         if stack.count() == 0:
#             stack.push(char)
#         else:
#             if Stack.top_stack == char:
#                 stack.push(char)
#             else:
#                 stack.pop()

# if stack.count() == 0:
#     print('VALID')
# else:
#     print('INVALID')

# @dataclass
# class Bag:
#     quantity: int # số lượng vật chứa
#     weight: float # khối lượng của các vật chứa

#     def __str__(self):
#         return f'{self.quantity} {self.weight}'

# stack_bag = Stack[Bag]()
# '''
# Nhập vào từng cái Bag có khối lượng weight và số lượng quantity

# Khi nhập các túi vào phải đảm bảo túi nhỏ nằm trên túi lơn hơn
# '''

# n=int(input())

# while n:
#     weight, quantity = map(float, input().split())
#     bag = Bag(quantity=quantity, weight=weight)
#     if stack_bag.count() != 0:
#         top_bag: Bag = stack_bag.top_stack.data
#         if bag.quantity*bag.weight <= top_bag.quantity*top_bag.weight:
#             stack_bag.push(bag)
#     else:
#         stack_bag.push(bag)
#     n-=1

# stack_bag.list_all()
stack_op = Stack[str]()
expression = input()[::-1]

value = 0
stack_op.push('')
for char in expression:
    if stack_op.count() != 0:
        if char == '+':
            value += float(stack_op.pop())
        elif char == '-':
            value -= float(stack_op.pop())
        else:
            stack_op.top_stack.data += char
    else:
        stack_op.push(char)

print(value)


