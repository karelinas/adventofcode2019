#!/usr/bin/env python3
#
# Run with: python3 b.py < input.txt

import sys
from vm import run

program = [int(n) for n in next(sys.stdin).split(',')]
TARGET = 19690720
for verb in range(0, 100):
    for noun in range(0, 100):
        program[1] = noun
        program[2] = verb
        mem = run(list(program))
        if mem[0] == TARGET:
            print(100 * noun + verb)
            break

