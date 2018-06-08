"""
FIFO Queue implemented using singly linked list.

Summary:

    Supports enqueue (to back) and dequeue (from front).

Characteristics:

    Enqueue:
        Worst Time: O(1)
    Dequeue:
        Worst Time: O(1)
"""

from data_structures.linked_list import LinkedList


class FIFOQueue(object):

    def __init__(self):
        self.list = LinkedList()

    def enqueue(self, item):
        self.list.append_right(item)

    def dequeue(self):

        if not self.list.n:
            raise EmptyQueueException

        return self.list.pop(0)


class EmptyQueueException(Exception):
    pass
