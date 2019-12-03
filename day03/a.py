import sys
from operator import add

def manhattan_distance(point):
    return abs(point[0]) + abs(point[1])

def translate(point, vector):
    return tuple(map(add, point, vector))

DIRECTIONS = {
    'U': ( 0,  1),
    'D': ( 0, -1),
    'L': (-1,  0),
    'R': ( 1,  0)
}
def line(instructions):
    pos = (0, 0)
    path = set()
    for instruction in instructions:
        direction = instruction[0]
        distance = int(instruction[1:])
        for _ in range(0, distance):
            pos = translate(pos, DIRECTIONS[direction])
            path.add(pos)
    return path

def intersections(lines):
    return lines[0].intersection(*lines[1:])

def closest_to_origin(points):
    return sorted(points, key=manhattan_distance)[0]

lines = []
for input_line in sys.stdin:
    instructions = [item.strip() for item in input_line.split(',')]
    lines.append(line(instructions))
print(manhattan_distance(closest_to_origin(intersections(lines))))
