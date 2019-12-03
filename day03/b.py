import sys
from operator import add

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
    steps = 0
    path = dict()
    for instruction in instructions:
        direction = instruction[0]
        distance = int(instruction[1:])
        for _ in range(0, distance):
            pos = translate(pos, DIRECTIONS[direction])
            steps = steps + 1
            if pos not in path:
                path[pos] = steps
    return path

def intersections(lines):
    return lines[0].intersection(*lines[1:])

def closest_by_steps(points, *lines):
    return sorted(points, key=lambda x: sum(l.get(x) for l in lines))[0]

lines = []
for input_line in sys.stdin:
    instructions = [item.strip() for item in input_line.split(',')]
    lines.append(line(instructions))
closest_point = closest_by_steps(intersections([set(l.keys()) for l in lines]), *lines)
print(sum(l.get(closest_point) for l in lines))
