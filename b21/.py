from typing import (
    TypeVar,
    Generic,
    Optional
)

TemplateQueue = TypeVar('TemplateQueue')


class Node(Generic[TemplateQueue]):
    def __init__(self, data: TemplateQueue):
        self.data = data
        self.next = None
        self.prev = None


class Queue(Generic[TemplateQueue]):
    def __init__(self):
        self.first: Optional[Node[TemplateQueue]] = None
        self.last: Optional[Node[TemplateQueue]] = None

    def is_empty(self):
        return self.first is None

    def add_queue(self, data: TemplateQueue):
        new_node = Node(data)
        if self.last is None:
            self.first = self.last = new_node
        else:
            self.last.next = new_node
            new_node.prev = self.last
            self.last = new_node

    def pop_queue(self):
        if self.is_empty():
            return None
        removed_node_first = self.first
        self.first = self.first.next
        if self.first is not None:
            self.first.prev = None
        else:
            self.last = None
        return removed_node_first.data

from dataclasses import dataclass

@dataclass
class Author:
    name: str
    birth: str

@dataclass
class Book:
    name: str
    publish: str
    author: Author

queue = Queue[Book]()