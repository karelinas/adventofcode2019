#!/usr/bin/env python3
#
# Run with: python3 a.py < input.txt

import math
import sys

def fuel_required(module_mass):
    return math.floor(module_mass / 3) - 2

assert fuel_required(12) == 2
assert fuel_required(14) == 2
assert fuel_required(1969) == 654
assert fuel_required(100756) == 33583

print(sum((fuel_required(int(line.strip())) for line in sys.stdin)))
