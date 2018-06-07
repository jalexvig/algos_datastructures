"""
Topological sort using depth first search in a graph.

Summary:
    
    DFS through graph. For each node mark it temporarily before processing neighbors. If any node has a temporary mark
    before it is processed, there is a cycle. When finished processing a node add it to the output list.

Characteristics:

    * n number nodes
    * e number edges

    Worst Time: O(n + e)

Other:
    
    * Kahn's algorithm
"""

from collections import defaultdict


def topo_sort_dfs(graph: dict):

    # 0 means unvisited, 1 is temporary mark to detect cycles, 2 means node has been completely resolved
    markings = defaultdict(int)
    output = []

    def traverse(node: str):
        """Process a node and recurse over its neighbors."""

        if markings[node] == 2:
            return

        markings[node] = 1

        for neighbor in graph.get(node, []):

            mark = markings[neighbor]

            # This node has already been fully processed
            if mark == 2:
                continue

            if mark == 1:
                raise ValueError('Cycle detected with node {}'.format(neighbor))

            traverse(neighbor)

        output.append(node)
        markings[node] = 2

    for node in graph:
        traverse(node)

    return output


if __name__ == '__main__':

    graph = {'a': 'bcd',
             'b': 'cd',
             'c': 'd',
             'e': 'f',
             'f': 'c'}

    print(topo_sort_dfs(graph))
