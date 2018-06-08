"""
Find the minimal path from source to destination.

Summary:

    Greedily search through graph choosing the next node based on which has the minimum distance. This works only for a
    non-negative weighted graph.

Characteristics:

    * n number nodes
    * e number edges

    Worst Time: O(n ** 2) or O(n e loge) if using priority queue

Other:

    * Bellman-Ford slower but handles negative weights
"""

from collections import defaultdict


def djikstra(graph: dict, source: str, destination: str):

    # TODO(jalex): improve this with a priority q (implementing modify operation)
    # TODO(jalex): Change this to be directed
    # TODO(jalex): Update this to be all destinations

    distances = defaultdict(lambda: float('inf'))
    distances[source] = 0

    processed = set()

    current = source

    while current != destination:

        for neighbor, dist in graph[current]:
            distances[neighbor] = min(distances[neighbor], distances[current] + dist)

        processed.add(current)

        while current in processed:
            distances.pop(current)
            try:
                current = min(distances.items(), key=lambda x: x[1])[0]
            except ValueError:
                return

    return distances[destination]


if __name__ == '__main__':

    import copy

    graph = {'a': [('b', 2), ('c', 5), ('d', 9)],
             'b': [('c', 2), ('d', 6)],
             'c': [('d', 5)],
             'e': [('f', 1)],
             'f': [('c', 0)]}

    # make this an graph undirected
    for node, neighbor_tups in copy.deepcopy(graph).items():
        for neighbor, dist in neighbor_tups:
            graph.setdefault(neighbor, []).append((node, dist))

    print(djikstra(graph, 'a', 'd'))
