import sys
from a import read_graph

def full_path(graph, node):
    path = set()
    while node in graph:
        node = graph.get(node)
        path.add(node)
    return path

def node_distance(graph, node1, node2):
    return len(set.symmetric_difference(full_path(graph, node1),
                                        full_path(graph, node2)))

graph = read_graph(sys.stdin)
print(node_distance(graph, "YOU", "SAN"))
