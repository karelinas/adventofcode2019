#!/usr/bin/env python3
#
# Run with: python3 a.py < input.txt

import sys
from vm import run

program = [int(n) for n in next(sys.stdin).split(',')]
program[1] = 12
program[2] = 2
mem = run(program)
print(mem[0])

