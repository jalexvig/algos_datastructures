"""
Sort array.

Summary:

    This algorithm works by iteratively scanning for the smallest remaining element and moving it into place.

Characteristics:

    * n number elements

    Worst Time: O(n ** 2)

    Stable: False (can be made stable)
"""


def selection_sort(l: list):

    n = len(l)

    for i in range(n - 1):
        idx_min = i
        for j in range(i + 1, n):
            if l[j] < l[idx_min]:
                idx_min = j
        l[i], l[idx_min] = l[idx_min], l[i]


if __name__ == '__main__':

    l = [3, 1, 2]
    selection_sort(l)
    print(l)
