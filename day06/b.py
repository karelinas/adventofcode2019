import sys

def first_common_ancestor(graph, child1, child2):
    # first make a list of all ancestors for child 1
    child1_ancestors = []
    child = graph.get(child1)
    while child in graph:
        child1_ancestors.append(child)
        child = graph.get(child)

    # then find the first shared ancestor
    child = graph.get(child2)
    while child in graph:
        if child in child1_ancestors:
            return child
        child = graph.get(child)

    return None


def distance_to_ancestor(graph, child, ancestor):
    distance = 0
    while child != ancestor:
        child = graph.get(child)
        distance += 1
    return distance

graph = {}

for line in sys.stdin:
    line = line.strip()
    if not len(line):
        continue
    parent, child = line.split(')')
    graph[child] = parent

common_ancestor = first_common_ancestor(graph, "YOU", "SAN")
distance_to_santa = (distance_to_ancestor(graph, "YOU", common_ancestor) +
                     distance_to_ancestor(graph, "SAN", common_ancestor) - 2)

print(distance_to_santa)
