"""
Sort array.

Summary:

    1. Pick a "pivot" element at random
    2. Recurse on elements less than pivot
    3. Recurse on elements greater than or equal to pivot
    4. Combine 2, pivot, and 3

Characteristics:

    * n number elements

    Worst Time: O(n ** 2)
    Average Time: O(n logn)

    Stable: True (False in efficient implementations)
"""


def quick_sort(a: list):

    if len(a) <= 1:
        return a

    pivot = a.pop()

    return quick_sort([x for x in a if x < pivot]) + [pivot] + quick_sort([x for x in a if x >= pivot])


if __name__ == '__main__':

    print(quick_sort([4, 1, 2, 3, 5]))
