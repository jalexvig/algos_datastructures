

def merge_sort(l):
    """
    Divide and conquer until sorted.

    :param l: list to sort.
    :return: sorted list.
    """

    if len(l) <= 1:
        return l

    idx_split = len(l) // 2

    sorted1 = merge_sort(l[:idx_split])
    sorted2 = merge_sort(l[idx_split:])

    return merge(sorted1, sorted2)


def merge(l1, l2):
    """
    Merge two sorted lists into a single sorted list.

    :param l1: sorted list.
    :param l2: sorted list.
    :return: sorted list with all elements from l1 and l2.
    """

    l = [None] * (len(l1) + len(l2))

    i, j = 0, 0

    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            l[i + j] = l1[i]
            i += 1
        else:
            l[i + j] = l2[j]
            j += 1

    idx, l_inp = (i, l1) if i < len(l1) else (j, l2)
    for k in range(1, len(l_inp) - idx + 1):
        l[-k] = l_inp[-k]

    return l


if __name__ == '__main__':

    print(merge_sort([4, 1, 2, 3, 5]))

