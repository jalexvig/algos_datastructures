"""
Map backed with hashing.

Summary:

    1. Closed hash: if there is something in the bucket deterministically figure out a new hash.
    2. Open hash: use linked lists in the bucket (means need pointer lookup and may leave hash table).

    Need to resize as hash table fills up since a full hash table can lead to lots of hash collisions (closed hashing)
    or long lists (open hashing).

    For closed hashing the choice of probing algorithm (to determine next hash on collision) is important. Linear
    probing, for example, is bad because it increases the average number of hash collisions in future operations.

Characteristics:

    * n number

    Get:
        Worst Time: O(n)
        Average Time: O(1)
    Set:
        Worst Time: O(n)
        Average Time: O(1) amortized
    Pop:
        Worst Time: O(n)
        Average Time: O(1) amortized
"""


class HashMap(object):
    """Closed hash map."""

    def __init__(self, capacity=10, upsize=2/3, downsize=0.25):

        self.min_capacity = capacity
        self.capacity = capacity
        self.upsize = upsize
        self.downsize = downsize

        self.size = 0

        self.array = [None] * self.capacity

    def __str__(self):

        return str(self.array)

    def check_capacity(self):

        new_capacity = None

        if self.size >= self.capacity * self.upsize:
            new_capacity = self.capacity * 2
        elif self.size <= self.capacity * self.downsize and self.capacity // 2 >= self.min_capacity:
            new_capacity = self.capacity // 2

        if new_capacity is not None:
            old_array = self.array

            self.array = [None] * new_capacity

            self.capacity = new_capacity

            for tup in old_array:
                if tup is None:
                    continue

                self[tup[0]] = tup[1]

    def get_idx(self, key, use_removed=False):
        """Get array index of existing key or place to put new entry."""

        h = hash(key) % self.capacity
        entry = self.array[h]

        while entry is not None:

            if entry is REMOVED:
                if use_removed:
                    break
            elif entry[0] == key:
                break

            # linear probing
            h = (h + 1) % self.capacity
            entry = self.array[h]

        return h

    def __setitem__(self, key, value):

        self.check_capacity()

        idx = self.get_idx(key, use_removed=True)

        self.array[idx] = (key, value)

    def __getitem__(self, key):

        idx = self.get_idx(key)

        tup = self.array[idx]

        if tup is None:
            raise KeyError

        return tup[1]

    def pop(self, key):

        idx = self.get_idx(key)

        tup = self.array[idx]

        if tup is None:
            raise KeyError

        self.array[idx] = REMOVED


class Removed(object):
    pass


REMOVED = Removed()


if __name__ == '__main__':

    # can set PYTHONHASHSEED=0 env variable to check this

    hm = HashMap(capacity=5)
    hm['a'] = 3
    hm['b'] = 4
    hm['c'] = 5

    print('getting')

    print(hm['a'], hm['b'], hm['c'])

    hm.pop('a')
    print(hm['b'])

    hm['a'] = 6

    print(hm)
