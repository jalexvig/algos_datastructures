
def bubble_sort(l):

    n = len(l)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]

    return l


if __name__ == '__main__':

    l = [3, 2, 1]
    bubble_sort(l)
    print(l)
