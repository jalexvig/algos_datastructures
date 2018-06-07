"""
Sort array.

Summary:

    Swap pairs of elements in array. At the end of each iteration through the array the next highest element is in
    place.

Characteristics:

    * n number elements

    Worst Time: O(n ** 2)

    Stable: True
"""


def bubble_sort(l: list):

    n = len(l)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]


if __name__ == '__main__':

    l = [3, 2, 1]
    bubble_sort(l)
    print(l)
