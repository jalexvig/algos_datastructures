"""
Lists implemented using a fictional array (a Python list).

Summary:

    Supports deleting at an index and inserting at an index.

Characteristics:

    * n number elements

    Index:
        Worst Time: O(1)
    Append (right):
        Worst Time: O(1)
    Pop (right):
        Worst Time: O(1)
    Delete:
        Worst Time: O(n)
    Insert:
        Worst Time: O(n)
"""


class ArrayList(object):

    def __init__(self, capacity=10, min_capacity=10):

        self.min_capacity = min_capacity
        self.capacity = capacity
        self.size = 0

        self.array = [None] * self.capacity

    def __str__(self):

        return str(self.array[:self.size])

    def __getitem__(self, idx):

        if not isinstance(idx, int):
            raise TypeError

        if idx >= self.size:
            raise IndexError

        return self.array[idx]

    def check_size(self):

        if self.size == self.capacity:
            self.capacity *= 2
            new_array = [None] * self.capacity
            new_array[:self.size] = self.array
            self.array = new_array

        if self.capacity >= 4 * self.min_capacity and self.size <= self.capacity // 4:
            self.capacity //= 2
            self.array = self.array[:self.capacity]

    def append(self, val):

        self.check_size()

        self.array[self.size] = val

        self.size += 1

    def insert(self, idx, val):

        if idx < -self.size or idx > self.size:
            raise IndexError

        # self.size is valid value for idx so can't mod all valid positive numbers
        if idx < 0:
            idx %= self.size

        self.check_size()

        self.array[idx + 1: self.size + 1] = self.array[idx: self.size]
        self.array[idx] = val

        self.size += 1

    def pop(self, idx=-1):

        if self.size == 0:
            raise EmptyListException

        if idx < -self.size or idx >= self.size:
            raise IndexError

        idx %= self.size

        val = self[idx]

        self.array[idx: self.size - 1] = self.array[idx + 1: self.size]

        self.size -= 1

        self.check_size()

        return val


class EmptyListException(Exception):
    pass


if __name__ == '__main__':

    l = ArrayList(capacity=6, min_capacity=1)
    l.insert(0, 2)
    l.insert(0, 1)
    l.append(3)
    l.insert(3, 4)
    l.insert(4, 5)
    l.insert(5, 7)
    l.insert(5, 6)
    l.append(8)
    print(l, l.array)

    l.pop(1)  # 2
    l.pop(3)  # 5
    l.pop(1)  # 3
    l.pop(1)  # 4
    l.pop(0)  # 1
    l.pop(-1)  # 8
    print(l, l.array)
