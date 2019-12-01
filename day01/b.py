#!/usr/bin/env python3
#
# Run with: python3 b.py < input.txt

import math
import sys

def fuel_for_mass(mass):
    return math.floor(mass / 3) - 2

def total_fuel_required(mass):
    added_fuel = fuel_for_mass(mass)
    if added_fuel <= 0:
        return 0
    return added_fuel + total_fuel_required(added_fuel)

assert fuel_for_mass(12) == 2
assert fuel_for_mass(14) == 2
assert fuel_for_mass(1969) == 654
assert fuel_for_mass(100756) == 33583

assert total_fuel_required(14) == 2
assert total_fuel_required(1969) == 966
assert total_fuel_required(100756) == 50346

fuel_required = sum((total_fuel_required(int(line.strip())) for line in sys.stdin))
print(fuel_required)

