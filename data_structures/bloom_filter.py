"""
Bloom filter for testing membership with no false negatives.

Summary:

    1. Condense an element down to a few array indices using corresponding number of hash functions.
    2. Set these bits in the boolean array.
    3. Any bit not set in the array means the corresponding element is not in the filter.

Characteristics:

    * m number bits in array
    * n number members
    * k number hashes

    Worst Space: O(m)

    False Positive Rate: (1 - (1 - 1/m) ** (k n)) ** k

    Add:
        Worst Time: O(k)
    Search:
        Worst Time: O(k)
"""


class BloomFilter(object):

    def __init__(self, num_hashes=5, size=30):

        assert num_hashes >= 1

        self.num_hashes = num_hashes
        self.size = size

        self.array = [0] * size

    def __contains__(self, item):

        # no false negatives but can have false positives

        for i in self.calculate_indices(item):
            if not self.array[i]:
                return False

        return True

    def calculate_indices(self, item):

        h = hash(item)

        for _ in range(self.num_hashes - 1):
            # hash of (small) int is the same int, so convert them to strings
            h = hash(str(h))
            yield h % self.size

    def add(self, item):

        for i in self.calculate_indices(item):
            self.array[i] = 1

    def update(self, iterable):

        for x in iterable:
            self.add(x)


if __name__ == '__main__':

    import string

    bf = BloomFilter(num_hashes=8, size=100)

    st = set()

    bf.update(string.ascii_lowercase[:20])

    n = 100000
    s = 0
    for i in range(n):
        s += str(i) in bf

    print('False positive rate: {}'.format(s / n))
