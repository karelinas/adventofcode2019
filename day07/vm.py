from inspect import signature

##############################
# CPU DATA
##############################
class Cpu():
    def __init__(self, memory, input_values):
        self.memory = memory
        self.pc = 0
        self.input_values = input_values
        self.output_values = []
        self.waiting_for_input = False
        self.exit_flag = False


##############################
# ADDRESSING MODES
##############################

def automatic_addressing(instr):
    def _instruction(cpu, addr_modes):
        instruction_signature = signature(instr)
        operand_count = len(instruction_signature.parameters)
        operands = []
        cpu.pc += 1
        for op in range(operand_count):
            operands.append(cpu.memory[cpu.pc] if addr_modes[op] else cpu.memory[cpu.memory[cpu.pc]])
            cpu.pc += 1
        value_out = instr(*operands)
        if value_out is not None:
            cpu.memory[cpu.memory[cpu.pc]] = value_out
            cpu.pc += 1
        return cpu
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

def getint(cpu, addr_modes) -> Cpu:
    addr_out = cpu.memory[cpu.pc+1]
    if cpu.input_values:
        cpu.memory[addr_out] = cpu.input_values.pop()
        cpu.pc += 2
    else:
        cpu.waiting_for_input = True
        cpu.exit_flag = True
    return cpu

def putint(cpu, addr_modes) -> Cpu:
    operand1 = cpu.memory[cpu.pc+1] if addr_modes[0] else cpu.memory[cpu.memory[cpu.pc+1]]
    cpu.output_values.append(operand1)
    cpu.pc += 2
    return cpu

def jnz(cpu, addr_modes) -> Cpu:
    param1 = cpu.memory[cpu.pc+1] if addr_modes[0] else cpu.memory[cpu.memory[cpu.pc+1]]
    param2 = cpu.memory[cpu.pc+2] if addr_modes[1] else cpu.memory[cpu.memory[cpu.pc+2]]
    if param1:
        cpu.pc = param2
    else:
        cpu.pc += 3
    return cpu

def jz(cpu, addr_modes) -> Cpu:
    param1 = cpu.memory[cpu.pc+1] if addr_modes[0] else cpu.memory[cpu.memory[cpu.pc+1]]
    param2 = cpu.memory[cpu.pc+2] if addr_modes[1] else cpu.memory[cpu.memory[cpu.pc+2]]
    if not param1:
        cpu.pc = param2
    else:
        cpu.pc += 3
    return cpu

@automatic_addressing
def slt(operand1, operand2) -> int:
    return int(operand1 < operand2)

@automatic_addressing
def equ(operand1, operand2) -> int:
    return int(operand1 == operand2)

def halt(cpu, addr_modes):
    cpu.exit_flag = True
    cpu.pc += 1
    return cpu

##############################
# PROGRAM EXECUTION
##############################

INSTRUCTION_TABLE = {
    1: add,
    2: mul,
    3: getint,
    4: putint,
    5: jnz,
    6: jz,
    7: slt,
    8: equ,
    99: halt
}

def decode(code):
    opcode = code % 100
    code //= 100
    addr_modes = []
    for _ in range(0, 3):
        addr_modes.append(code % 10)
        code //= 10
    return (opcode, addr_modes)

def dispatch(cpu, opcode, addr_modes):
    return INSTRUCTION_TABLE[opcode](cpu, addr_modes)

def run(cpu):
    while not cpu.exit_flag:
        opcode, addr_modes = decode(cpu.memory[cpu.pc])
        cpu = dispatch(cpu, opcode, addr_modes)
    return cpu

def resume(cpu, input_value):
    cpu.exit_flag = False
    cpu.waiting_for_input = False
    cpu.input_values.append(input_value)
    return run(cpu)


