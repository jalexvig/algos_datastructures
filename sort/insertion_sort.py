"""
Sort array.

Summary:

    Move one element at a time into the correct position with respect to the preceding elements of the array.

Characteristics:

    * n number elements

    Worst Time: O(n ** 2)

    Stable: True
"""


def insertion_sort(l: list):

    # i is index of element in question
    for i in range(len(l)):
        # j is index of element (in sorted prefix) we are switching with
        for j in range(i-1, -1):
            if l[i] < l[j]:
                l[j] = l[i]
                i = j


if __name__ == '__main__':

    l = [3, 2, 1]
    insertion_sort(l)
    print(l)
