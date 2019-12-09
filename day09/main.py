import sys
from vm import run, Cpu

program = [int(n) for n in open('input.txt').read().strip().split(',')]
for _ in range(100000):
    program.append(0)

# Part 1
cpu = Cpu(list(program), [1])
cpu = run(cpu)
print(cpu.output_values[0])

# Part 2
cpu = Cpu(list(program), [2])
cpu = run(cpu)
print(cpu.output_values[0])
