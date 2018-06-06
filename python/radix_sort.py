from collections import defaultdict


def radix_sort(l):

    l = [bin(x)[2:] for x in l]

    max_len = max(map(len, l))

    l = [x.zfill(max_len) for x in l]

    for i in range(1, max_len+1):
        d = defaultdict(list)
        for b in l:
            d[b[-i]].append(b)

        l = [x for j in range(10) for x in d[str(j)]]

    return [int(b, 2) for b in l]


if __name__ == '__main__':

    l = [3, 4, 2, 1, 5, 0]

    print(radix_sort(l))
