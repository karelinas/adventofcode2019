import sys
from itertools import permutations
from vm import run, resume, Cpu

program = [int(n) for n in open('input.txt').read().split(',')]

largest_output = 0
input_combinations = permutations([5, 6, 7, 8, 9])
for combo in input_combinations:
    cpus = [
        Cpu(list(program), [combo[0]]),
        Cpu(list(program), [combo[1]]),
        Cpu(list(program), [combo[2]]),
        Cpu(list(program), [combo[3]]),
        Cpu(list(program), [combo[4]])
    ]
    for idx in range(len(cpus)):
        cpus[idx] = run(cpus[idx])
    previous_output = 0
    while cpus[4].waiting_for_input:
        for idx in range(len(cpus)):
            cpus[idx] = resume(cpus[idx], previous_output)
            previous_output = cpus[idx].output_values.pop()
    largest_output = max(largest_output, previous_output)

print(largest_output)

