import sys
from itertools import permutations
from vm import run, Cpu

program = [int(n) for n in open('input.txt').read().split(',')]

largest_output = 0
input_combinations = permutations([0, 1, 2, 3, 4])
for combo in input_combinations:
    previous_output = 0
    for phase_setting in combo:
        input_values = [previous_output, phase_setting]
        cpu = Cpu(list(program), input_values)
        cpu = run(cpu)
        previous_output = cpu.output_values.pop()
    largest_output = max(largest_output, previous_output)

print(largest_output)

