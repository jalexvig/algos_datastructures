"""
Find a minimal spanning tree in a graph.

Summary:

    Until a spanning tree is reached get edge with smallest weight. If this edge connects separate components, add it to
    the spanning tree. Otherwise discard it.

Characteristics:

    * n number nodes
    * e number edges

    Worst Time: O(e loge) == O(e logn)
"""

from collections import deque


def kruskal(graph: list):

    edges = deque(sorted(graph))
    trees = {}

    mst = []

    for edge_tup in graph:
        trees.setdefault(edge_tup[1], {edge_tup[1]})
        trees.setdefault(edge_tup[2], {edge_tup[2]})

    n_vertices = len(trees)

    while edges:

        w, n1, n2 = edges.popleft()

        if n2 in trees[n1]:
            continue

        mst.append((w, n1, n2))

        trees[n1].update(trees[n2])

        if len(trees[n1]) == n_vertices:
            return mst

        trees[n2] = trees[n1]

    return


if __name__ == '__main__':

    graph = [(2, 'a', 'b'), (5, 'a', 'c'), (9, 'a', 'd'),
             (2, 'b', 'c'), (6, 'b', 'd'), (5, 'c', 'd'),
             (1, 'e', 'f'), (10, 'f', 'c')]

    print(kruskal(graph))
