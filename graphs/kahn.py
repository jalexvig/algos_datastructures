"""
Kahn's algorithm for topological sort.

Summary:

    1. Find nodes that have no dependencies and add them to queue.
    2. Remove those nodes as dependencies for other nodes.
    3. Repeat this until all nodes have been placed in queue.

Characteristics:

    * n number nodes
    * e number edges

    Worst Time: O(n + e)

Other:

    * Topological sort DFS
"""

from collections import deque


def kahn(graph: dict):

    dependencies = {}

    for parent, children in graph.items():
        dependencies.setdefault(parent, [])
        for child in children:
            dependencies.setdefault(child, []).append(parent)

    q = deque(child for child, parents in dependencies.items() if not parents)

    res = []

    while q:

        parent = q.popleft()
        dependencies.pop(parent)

        for child in graph.get(parent, []):
            dependencies[child].remove(parent)

        res.append(parent)

        if not q:
            q = deque(child for child, parents in dependencies.items() if not parents)

    if dependencies:
        raise CycleDetectedException

    return res


class CycleDetectedException(Exception):
    pass


if __name__ == '__main__':

    graph = {'a': 'bcd',
             'b': 'cda',
             'c': 'd',
             'e': 'f',
             'f': 'c'}

    print(kahn(graph))
