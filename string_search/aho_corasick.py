"""
Search for patterns in text.

Summary:

    1. Construct a [trie](https://en.wikipedia.org/wiki/Trie) of the patterns.
    2. Recursively determine fail states by looking at parent's fail state.
    3. Use trie to create DFA with non-matches following to fail states.

Characteristics:

    * `m` = length of all patterns -- O(m) incurred when building the trie
    * `n` = length of search text
    * `z` = number matches

    Worst Time: O(m + n + z)

Other:

    * This is KMP extended to multiple patterns.
"""

from collections import deque


class Node:

    def __init__(self):

        self.paths = {}
        self.out = []
        self.fail = None

    def __contains__(self, item):
        return item in self.paths

    def __getitem__(self, item):
        return self.paths[item]


def construct_trie(*patterns: list):

    root = Node()

    for pattern in patterns:
        node = root
        for c in pattern:
            node = node.paths.setdefault(c, Node())
        node.out.append(pattern)

    return root


def update_failed_states(root: Node):
    """Mark fail states for all nodes in graph."""

    q = deque()

    for node_level_1 in root.paths.values():
        node_level_1.fail = root
        q.append(node_level_1)

    while q:
        node_parent = q.popleft()
        for char, node_child in node_parent.paths.items():
            node_fail = node_parent.fail
            # fail node is node of maximal suffix for node_child
            while node_fail and char not in node_fail:
                node_fail = node_fail.fail

            node_child.fail = node_fail[char] if node_fail else root
            # this maximal suffix may be word
            node_child.out += node_child.fail.out

            q.append(node_child)


def find(root: Node, text: str):
    """Find instances of patterns defined by root in a string."""

    res = []
    node = root

    for c in text:

        while node and c not in node:
            node = node.fail

        # No suffix exists... skip this character
        if not node:
            node = root
            continue

        node = node[c]

        if node.out:
            res += node.out

    return res


if __name__ == '__main__':

    patterns = ['a', 'abc', 'bcd', 'abcdef', 'cdefg']
    text = 'eaabcdabcdefg'

    root = construct_trie(*patterns)

    update_failed_states(root)

    print(*find(root, text))
