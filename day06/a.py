import sys

def ancestor_count(graph, child):
    parent = graph.get(child, None)
    if not parent:
        return 0
    return 1 + ancestor_count(graph, parent)

graph = {}

for line in sys.stdin:
    line = line.strip()
    if not len(line):
        continue
    parent, child = line.split(')')
    graph[child] = parent

orbit_count = sum((ancestor_count(graph, child) for child in graph.keys()))

print(orbit_count)
