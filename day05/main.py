import sys
from vm import run

program = [int(n) for n in open('input.txt').read().split(',')]
run(program)

