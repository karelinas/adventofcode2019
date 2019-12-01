#!/usr/bin/env python3
#
# Run with: python3 a.py < input.txt

import sys

def fuel_for_mass(module_mass):
    return module_mass // 3 - 2

assert fuel_for_mass(12) == 2
assert fuel_for_mass(14) == 2
assert fuel_for_mass(1969) == 654
assert fuel_for_mass(100756) == 33583

if __name__ == '__main__':
    print(sum((fuel_for_mass(int(line)) for line in sys.stdin)))
