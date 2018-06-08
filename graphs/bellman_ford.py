"""
Find shortest distances to all nodes in graph from a source node.

Summary:

    Start with distance to source as 0. Once for every other vertex: update **all** distances using the weights from the
    graph. This ensures that all paths are accounted for since making one hop per iteration means can fully traverse a
    linear graph.

    If distances can be reduced after this, there is a negative weight cycle somewhere in the graph.

Characteristics:

    * n number nodes
    * e number edges

    Worst Time: O(n e)

Other:

    * Djikstra's algorithm faster but can't handle negative weights
"""

from collections import defaultdict


def bellman_ford(graph: dict, source: str):

    distances = defaultdict(lambda: float('inf'))
    distances[source] = 0

    nodes = set()
    for n1, edges in graph.items():
        nodes.add(n1)
        for n2, _ in edges:
            nodes.add(n2)

    for _ in range(len(nodes) - 1):

        # tracking whether updated doesn't help worst time but can make big difference if graph not linear
        updated = False
        for n1, edges in graph.items():
            for n2, w in edges:
                if distances[n1] + w < distances[n2]:
                    distances[n2] = distances[n1] + w
                    updated = True

        if not updated:
            break

    for n1, edges in graph.items():
        for n2, w in edges:
            if distances[n1] + w < distances[n2]:
                raise NegativeWeightCycleException

    return distances


class NegativeWeightCycleException(Exception):
    pass


if __name__ == '__main__':

    graph = {'a': [('b', 2), ('c', 5), ('d', 9)],
             'b': [('c', 2), ('d', 6), ('a', -2)],
             'c': [('d', 5)],
             'e': [('f', 1)],
             'f': [('c', 0)]}

    print(bellman_ford(graph, 'a'))
