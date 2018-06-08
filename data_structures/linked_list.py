"""
Lists implemented using singly/doubly linked nodes.

Summary:

    Supports appending on either side, popping at an index, inserting at an index.

Characteristics:

    * n number elements

    Index:
        Worst Time: O(n)
    Search:
        Worst Time: O(n)
    Append left:
        Worst Time: O(1)
    Append right:
        Worst Time: O(1)
    Pop:
        Worst Time: O(n)
    Insert:
        Worst Time: O(n)
"""


class Node(object):

    def __init__(self, val, next_=None, prev=None):

        self.val = val

        self.next = next_
        self.prev = prev


class LinkedList(object):

    def __init__(self):

        self.head = None
        self.last = None
        self.n = 0

    def __str__(self):

        vals = []

        current = self.head
        while current is not None:
            vals.append(str(current.val))
            current = current.next

        return '-'.join(vals)

    def __getitem__(self, idx):

        if not isinstance(idx, int):
            raise TypeError

        if idx >= self.n:
            raise IndexError

        current = self.head
        for _ in range(idx):
            current = current.next

        return current

    def __contains__(self, item):

        current = self.head

        while current:
            if current.val == item:
                return True
            current = current.next

        return False

    def append_left(self, item):

        self.head = Node(item, self.head)

        if not self.n:
            self.last = self.head

        self.n += 1

    def append_right(self, item):

        node = Node(item, None)

        if self.n:
            self.last.next = node
        else:
            self.head = node

        self.last = node

        self.n += 1

    def pop(self, idx):

        if idx >= self.n:
            raise InvalidAccessException

        if idx == 0:
            val = self.head.val
            self.head = self.head.next
            self.n -= 1
            return val

        prev = self[idx - 1]

        val = prev.next.val

        if idx == self.n - 1:
            self.last = prev
        else:
            prev.next = prev.next.next

        self.n -= 1

        return val

    def insert(self, idx, val):

        if idx > self.n:
            raise InvalidAccessException

        if idx == 0:
            return self.append_left(val)
        if idx == self.n:
            return self.append_right(val)

        prev = self[idx - 1]

        prev.next = Node(val, prev.next)

        self.n += 1


class DoublyLinkedList(LinkedList):

    def __str__(self):

        vals = []

        current = self.last
        while current is not None:
            vals.append(str(current.val))
            current = current.prev

        rev_str = '-'.join(vals)
        forw_str = super().__str__()

        return forw_str + '\n' + rev_str

    def append_left(self, item):

        super().append_left(item)

        if self.head.next:
            self.head.next.prev = self.head

    def append_right(self, item):

        last_old = self.last

        super().append_right(item)

        if last_old:
            self.last.prev = last_old

    def pop(self, idx):

        super().pop(idx)

        if idx < self.n:
            if idx == 0:
                self.head.prev = None
            else:
                prev = self[idx - 1]
                prev.next.prev = prev

    def insert(self, idx, val):

        super().insert(idx, val)

        if idx > 0:
            prev = self[idx - 1]
            prev.next.prev = prev

        if idx < self.n - 1:
            curr = self[idx]
            curr.next.prev = curr


class InvalidAccessException(Exception):
    pass


if __name__ == '__main__':

    l = DoublyLinkedList()
    l.append_right(3)
    l.append_right(5)
    l.append_left(4)
    l.insert(1, 0)
    l.pop(2)
    assert 3 not in l
    print(l)
