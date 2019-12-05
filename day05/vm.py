from inspect import signature

##############################
# ADDRESSING MODES
##############################

def automatic_addressing(instr):
    def _instruction(addr_modes, mem, pc):
        instruction_signature = signature(instr)
        operand_count = len(instruction_signature.parameters)
        operands = []
        pc += 1
        for op in range(operand_count):
            operands.append(mem[pc] if addr_modes[op] else mem[mem[pc]])
            pc += 1
        value_out = instr(*operands)
        if value_out is not None:
            mem[mem[pc]] = value_out
            pc += 1
        return (mem, pc)
    return _instruction


##############################
# INSTRUCTIONS
##############################

@automatic_addressing
def add(operand1, operand2) -> int:
    return operand1 + operand2

@automatic_addressing
def mul(operand1, operand2) -> int:
    return operand1 * operand2

@automatic_addressing
def getint() -> int:
    return int(input("> "))

@automatic_addressing
def putint(operand1) -> None:
    print(operand1)

def jnz(addr_modes, mem, pc):
    param1 = mem[pc+1] if addr_modes[0] else mem[mem[pc+1]]
    param2 = mem[pc+2] if addr_modes[1] else mem[mem[pc+2]]
    if param1:
        return (mem, param2)
    else:
        return (mem, pc+3)

def jz(addr_modes, mem, pc):
    param1 = mem[pc+1] if addr_modes[0] else mem[mem[pc+1]]
    param2 = mem[pc+2] if addr_modes[1] else mem[mem[pc+2]]
    if not param1:
        return (mem, param2)
    else:
        return (mem, pc+3)

@automatic_addressing
def slt(operand1, operand2) -> int:
    return int(operand1 < operand2)

@automatic_addressing
def equ(operand1, operand2) -> int:
    return int(operand1 == operand2)

##############################
# PROGRAM EXECUTION
##############################

def decode(code):
    opcode = code % 100
    code //= 100
    addr_modes = []
    for _ in range(0, 3):
        addr_modes.append(code % 10)
        code //= 10
    return (opcode, addr_modes)

INSTRUCTION_TABLE = {
    1: add,
    2: mul,
    3: getint,
    4: putint,
    5: jnz,
    6: jz,
    7: slt,
    8: equ
}

def dispatch(opcode, addr_modes, mem, pc):
    if opcode not in INSTRUCTION_TABLE:
        return (False, mem, pc)
    mem, pc = INSTRUCTION_TABLE[opcode](addr_modes, mem, pc)
    return (True, mem, pc)

def run(mem):
    pc = 0
    while True:
        opcode, addr_modes = decode(mem[pc])
        cont, mem, pc = dispatch(opcode, addr_modes, mem, pc)
        if not cont:
            break
    return mem

