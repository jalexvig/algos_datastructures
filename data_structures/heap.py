"""
Min heap.

Summary:

    Optimal datastructure for accessing minimum element after pushes and pops. These are useful as priority queues. Two
    invariants are maintained through pushes/pops:

    1. Shape: complete binary tree (all nodes filled in until last level and then filled in order)
    2. Order: each parent node is less than its children

    The minimum element will then always be at the top of the heap.

Characteristics:

    * n number elements

    Pop:
        Worst Time: O(logn)
    Push:
        Worst Time: O(logn)
    Heapify:
        Worst Time: O(n) using sift-down method
    Search:
        Worst Time: O(n)
"""

import math


class Heap(object):

    def __init__(self, capacity=10, min_capacity=10):

        self.min_capacity = min_capacity
        self.capacity = capacity
        self.size = 0

        self.array = [None] * self.capacity

    def __str__(self):

        return str(self.array[:self.size])

    def __contains__(self, item):

        for i in range(self.size):
            if self.array[i] == item:
                return True

        return False

    def check_size(self):

        if self.size == self.capacity:
            self.capacity *= 2
            new_array = [None] * self.capacity
            new_array[:self.size] = self.array
            self.array = new_array

        if self.capacity >= 4 * self.min_capacity and self.size <= self.capacity // 4:
            self.capacity //= 2
            self.array = self.array[:self.capacity]

    @classmethod
    def heapify(cls, iterable, min_capacity=10):

        # O(n) since number nodes at each level shrinks moving up subtrees (exponential) much faster than number moves
        # required for a node at that level (linear)

        n = len(iterable)

        capacity = n + min_capacity

        heap = cls(capacity, min_capacity)

        heap.size = n
        heap.array[:n] = list(iterable)

        height = int(math.log2(heap.size))

        if height <= 0:
            return

        # sift non-leaf nodes down
        for lvl in range(height - 1, -1, -1):
            for idx in range(2 ** lvl - 1, 2 ** (lvl + 1) - 1):
                heap.sift_down(idx)

        return heap

    def push(self, val):

        self.check_size()

        self.array[self.size] = val
        self.size += 1

        self.sift_up()

    def sift_up(self, idx=-1):

        if idx < -self.size or idx >= self.size:
            raise IndexError

        idx %= self.size

        while idx != 0:
            idx_parent = (idx - 1) // 2
            if self.array[idx] < self.array[idx_parent]:
                self.array[idx], self.array[idx_parent] = self.array[idx_parent], self.array[idx]
                idx = idx_parent
            else:
                break

    def pop(self):

        if self.size == 0:
            raise IndexError

        val = self.array[0]

        # change first element to last so we can delete the min element
        self.array[0] = self.array[self.size - 1]

        self.size -= 1

        if self.size > 0:
            self.sift_down()

        self.check_size()

        return val

    def sift_down(self, idx=0):

        height = int(math.log2(self.size))

        # loop if idx not in bottom row
        while idx < 2 ** height:

            idx_child1 = idx * 2 + 1

            if idx_child1 >= self.size:
                break
            elif idx_child1 == self.size - 1:
                idx_child = idx_child1
            else:
                idx_child2 = idx * 2 + 2
                idx_child = idx_child1 if self.array[idx_child1] < self.array[idx_child2] else idx_child2

            if self.array[idx] > self.array[idx_child]:
                self.array[idx], self.array[idx_child] = self.array[idx_child], self.array[idx]
                idx = idx_child
            else:
                break


if __name__ == '__main__':

    import heapq
    import random

    ph = [random.randint(0, 99) for _ in range(10)]

    h = Heap.heapify(ph)
    heapq.heapify(ph)

    for _ in range(1000):
        if random.random() < 0.5 and h.size > 0:
            assert heapq.heappop(ph) == h.pop()
        else:
            elem = random.choice(list(range(100)))
            h.push(elem)
            heapq.heappush(ph, elem)

    h = Heap()
    h.push(3)
    h.push(2)
    h.push(1)
    h.push(0)
    h.pop()
    h.push(1.5)
    h.pop()
    print(h)
