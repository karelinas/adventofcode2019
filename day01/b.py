#!/usr/bin/env python3
#
# Run with: python3 b.py < input.txt

import sys
from a import fuel_for_mass

def total_fuel_required(mass):
    added_fuel = fuel_for_mass(mass)
    if added_fuel <= 0:
        return 0
    return added_fuel + total_fuel_required(added_fuel)

assert total_fuel_required(14) == 2
assert total_fuel_required(1969) == 966
assert total_fuel_required(100756) == 50346

if __name__ == '__main__':
    fuel_required = sum((total_fuel_required(int(line)) for line in sys.stdin))
    print(fuel_required)

