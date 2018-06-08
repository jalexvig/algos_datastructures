"""
Stack (LIFO) implemented using singly linked list.

Summary:

    Supports pushing to top of stack and popping off of top of stack.

Characteristics:

    Push:
        Worst Time: O(1)
    Pop:
        Worst Time: O(1)
"""

from data_structures.linked_list import LinkedList


class Stack:

    def __init__(self):
        self.list = LinkedList()

    def push(self, item):
        self.list.append_left(item)

    def pop(self):

        if self.list.n == 0:
            raise EmptyStackException

        return self.list.pop(0)


class EmptyStackException(Exception):
    pass
