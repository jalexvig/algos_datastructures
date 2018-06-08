"""
Sort an array.

Summary:

    This sort method pushes elements onto a min heap and then pops them off in increasing order.

Characteristics:

    * n number

    Worst Time: O(n logn)
"""

from data_structures.heap import Heap


def heap_sort(l: list):

    min_heap = Heap.heapify(l)

    res = []

    while min_heap.size > 0:
        res.append(min_heap.pop())

    return res


if __name__ == '__main__':

    l = [3, 2, 4, 1]
    res = heap_sort(l)
    print(res)
