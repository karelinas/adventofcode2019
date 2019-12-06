# draw.py

import sys

from graphviz import Digraph

g = Digraph(format="png")
g.attr(rankdir='BT')

for line in sys.stdin:
    line = line.strip()
    if not len(line):
        continue
    parent, child = line.split(')')
    g.edge(child, parent)

g.view()
