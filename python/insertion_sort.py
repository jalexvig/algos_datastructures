

def insertion_sort(l):

    # i is index of element in question
    for i in range(l):
        # j is index of element (in sorted prefix) we are switching with
        for j in range(i-1, -1):
            if l[i] < l[j]:
                l[j] = l[i]
                i = j


if __name__ == '__main__':

    l = [3, 2, 1]
    insertion_sort(l)
    print(l)
