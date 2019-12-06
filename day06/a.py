import sys

def ancestor_count(graph, child):
    parent = graph.get(child, None)
    if not parent:
        return 0
    return 1 + ancestor_count(graph, parent)

def read_graph(iterator):
    graph = {}
    for line in iterator:
        line = line.strip()
        if not len(line):
            continue
        parent, child = line.split(')')
        graph[child] = parent
    return graph

if __name__ == '__main__':
    graph = read_graph(sys.stdin)
    orbit_count = sum((ancestor_count(graph, child) for child in graph.keys()))
    print(orbit_count)
