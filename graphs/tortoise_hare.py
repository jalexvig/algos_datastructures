"""
Find a cycle in a sequence.

Summary:

    Move one pointer at a slow speed and another at a fast speed. If they ever point to the same object, there is a
    cycle. Derive cycle start point and cycle length accordingly.

Characteristics:

    * s cycle start position
    * l cycle length

    Worst Time: O(s + l)
"""


class Node(object):

    def __init__(self):
        self.next = None


def tortoise_hare_detect_cycle(node: Node):

    tortoise = node.next
    hare = tortoise.next

    while tortoise is not hare:
        if not hare.next or not hare.next.next:
            return

        tortoise = tortoise.next
        hare = hare.next.next

    # tortoise and hare at same point in cycle
    #
    # at this point the cycle length divides the tortoise's index (t)
    # t == hare - tortoise since hare moving twice as fast
    # sequence[cycle_start + t] == sequence[cycle_start]

    # reset tortoise
    # break hare position into cycle_start + x
    # because cycle_length divides hare position, hare must be cycle_start positions before (in cycle) the cycle_start
    # then can increment from beginning of sequence and from hare to find the position

    cycle_start = 0
    tortoise = node
    while tortoise is not hare:
        tortoise = tortoise.next
        hare = hare.next
        cycle_start += 1

    # hare and tortoise at cycle_start so can just move hare until it gets back to tortoise

    cycle_length = 1
    hare = tortoise.next
    while tortoise != hare:
        hare = hare.next
        cycle_length += 1

    return cycle_start, cycle_length


if __name__ == '__main__':

    first = Node()
    prev = first
    for i in range(9):
        node = Node()
        prev.next = node
        prev = node

    prev.next = first.next.next.next

    print(tortoise_hare_detect_cycle(first))
