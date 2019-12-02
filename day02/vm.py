##############################
# ADDRESSING MODES
##############################

def indirect_addressing(instr):
    def _instruction(mem, pc):
        operand1 = mem[mem[pc + 1]]
        operand2 = mem[mem[pc + 2]]
        addr_out = mem[pc + 3]
        mem[addr_out] = instr(operand1, operand2)
        return mem
    return _instruction


##############################
# INSTRUCTIONS
##############################

@indirect_addressing
def addi(operand1, operand2):
    return operand1 + operand2

@indirect_addressing
def muli(operand1, operand2):
    return operand1 * operand2


##############################
# PROGRAM EXECUTION
##############################

INSTRUCTION_TABLE = {
    1: addi,
    2: muli
}

def dispatch(mem, pc):
    opcode = mem[pc]
    if opcode not in INSTRUCTION_TABLE:
        return (False, mem)
    mem = INSTRUCTION_TABLE[opcode](mem, pc)
    return (True, mem)

def run(mem):
    pc = 0
    while True:
        cont, mem = dispatch(mem, pc)
        if not cont:
            break
        pc = pc + 4
    return mem


##############################
# "TESTS"
##############################

assert run([1, 0, 0, 0, 99]) == [2, 0, 0, 0, 99]
assert run([2, 3, 0, 3, 99]) == [2, 3, 0, 6, 99]
assert run([2, 4, 4, 5, 99, 0]) == [2, 4, 4, 5, 99, 9801]
assert run([1, 1, 1, 4, 99, 5, 6, 0, 99]) == [30, 1, 1, 4, 2, 5, 6, 0, 99]

