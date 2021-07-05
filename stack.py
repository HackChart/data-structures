from nodes import LinearNode
from exceptions import StackOverflowError, StackUnderflowError


class Stack:
    def __init__(self, limit=None):
        self.top_item = None
        self.size = 0
        self.limit = limit

    def is_empty(self):
        return self.size == 0

    def has_space(self):
        if self.limit:
            return self.limit > self.size
        else:
            return True

    def put(self, value):
        """Add an item to the top of the stack"""
        if self.has_space():
            item = LinearNode(value)
            item.set_next_node(self.top_item)
            self.top_item = item
            self.size += 1
        else:
            raise StackOverflowError

    def pop(self):
        """Removes and returns top item"""
        if self.is_empty():
            raise StackUnderflowError('Cannot return top item, stack empty')
        else:
            # get item to remove
            item = self.top_item
            # reset top item
            self.top_item = self.top_item.next_node
            self.size -= 1
            return item

    def peek(self):
        """Returns top item, stack unaltered"""
        if self.is_empty():
            raise StackUnderflowError('Cannot peek, stack empty')
        else:
            return self.top_item
