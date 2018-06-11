"""
Find a minimal spanning tree greedily.

Summary:

    Pick a node at random to start the MST and add all edges connected to it to a min heap.

    Until we reach a spanning tree:

    1. Pop minimal edge off of min heap and add it to MST.
    2. Add edges connected to new node if they don't form cycles and have lower weight than current estimate (for the
       new node in new edge).

Characteristics:

    * n number nodes
    * e number edges

    Worst Time: O(e logn)

Other:

    * Kruskal
"""

from data_structures.heap import Heap

import bisect


def get_first_idx(l, val):

    return bisect.bisect_left(l, val)


def prim(graph: list):

    # O(n logn)
    adj_list = sorted([x for w, n1, n2 in graph for x in [(n1, n2, w), (n2, n1, w)]])

    keys = [n1 for n1, n2, w in adj_list]

    vertices = [k1 for k1, k2 in zip(keys, keys[1:]) if k1 != k2]
    if vertices[-1] != keys[-1]:
        vertices.append(keys[-1])

    n = len(vertices)

    distances = [float('inf')] * n
    min_dist_heap = Heap.heapify(zip(distances, vertices[1:]))
    min_dist_heap.push((0, vertices[0]))

    mst = []

    candidate_edge = {v: None for v in vertices}

    # O(n) times till next for loop
    for i in range(n):
        # O(log n)
        w_curr, node_added = min_dist_heap.pop()

        # first edge will be None since just getting single vertex
        mst.append(candidate_edge.pop(node_added))

        idx_adj_list = bisect.bisect_left(keys, node_added)

        # O(e) times total in this block
        for n1, n2, w in adj_list[idx_adj_list:]:
            if n1 != node_added:
                break

            # already in mst
            if n2 not in candidate_edge:
                continue

            idx_dist = bisect.bisect_left(vertices, n2)
            if w < distances[idx_dist]:
                w0 = distances[idx_dist]
                distances[idx_dist] = w
                # O(logn)
                min_dist_heap.modify((w0, n2), (w, n2))
                candidate_edge[n2] = (n1, n2, w)

    return mst[1:]


if __name__ == '__main__':

    graph = [(2, 'a', 'b'), (5, 'a', 'c'), (9, 'a', 'd'),
             (2, 'b', 'c'), (6, 'b', 'd'), (5, 'c', 'd'),
             (1, 'e', 'f'), (10, 'f', 'c')]

    print(prim(graph))
