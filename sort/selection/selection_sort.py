

def selection_sort(l):
    """
    Swap minimum remaining element into correct place iteratively.

    :param l: list to sort.
    """

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
