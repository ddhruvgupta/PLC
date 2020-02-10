import sys
from WAEParser import parser
from WAELexer import lexer
import re
from collections import defaultdict
from pprint import pprint


def populate(data):
    out = []
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        if tok.type == 'REG':
            out.append(tok.value.upper())
    return out


def instruction(tree):
    instruction_set = defaultdict(list)
    init = []
    curr_instr = ""
    pattern = re.compile('[N][0-9]*[AB]*')
    for ea in tree:
        if curr_instr == "" and pattern.match(ea[0]):
            curr_instr = ea[0]
            instruction_set[curr_instr] = []
            instruction_set[curr_instr].append(ea[1])
        elif curr_instr != "" and pattern.match(ea[0]) is None:
            instruction_set[curr_instr].append(ea)
        elif curr_instr != "" and pattern.match(ea[0]):
            curr_instr = ea[0]
            instruction_set[curr_instr] = [ea[1]]
        else:
            init.append(ea)
    return init, instruction_set


def eval_expression(registers, instr_dict, init):
    for ea in init:
        if ea[0] == '=':
            registers[ea[1]] = ea[2]
        elif ea[0] == 'INC':
            registers[ea[1]] += 1
        elif ea[0] == 'DEC':
            registers[ea[1]] -= 1
        elif ea[0] == 'MOV':
            registers[ea[1]] = registers[ea[2]]

    labels = list(instr_dict.keys())

    for i in labels:
        run(registers, instr_dict, i)


def run(reg, instruction, index):
    # print("current instruction set: ", instruction[index])
    if isinstance(instruction[index], list):
        for ea in instruction[index]:
            if ea[0] == 'INC':
                reg[ea[1]] += 1
            elif ea[0] == 'DEC':
                if reg[ea[1]] > 0:
                    reg[ea[1]] -= 1
            elif ea[0] == 'MOV':
                reg[ea[1]] = reg[ea[2]]
            elif ea[0] == 'JMP':
                next_jump = ea[1]
                run(reg, instruction, next_jump)

            elif ea[0] == 'IF':
                if reg[ea[1]] == 0:
                    run(reg, instruction, ea[2][1])
                    run(reg, instruction, index)
                else:
                    continue
            elif ea[0] == "CON":
                print("R1 = " + str(reg["R1"]))
                exit()
            elif ea == "CON":
                print("R1 = " + str(reg["R1"]))
                exit()
    else:
        if instruction[index] == "CON":
            print("R1 = " + str(reg["R1"]))
            exit()
    return


def main():
    while True:
        if len(sys.argv) == 3:
            if sys.argv[1] == '-d':
                break
            else:
                print("usage is py -3 WAE.py -d p1.ram")
                exit()
        else:
            print("number of arguments is less")
            print("usage is py -3 WAE.py -d p1.ram")
            exit()

    filename = sys.argv[2]
    # filename = "p1.ram"
    with open(filename) as file_object:
        lines = file_object.readlines()

    tree = list()
    registers_list = []

    for line in lines:
        if line != '\n':
            tree.append(parser.parse(line))
            registers_list += populate(line)

    pprint(tree)
    registers = {registers_list[i]: 0 for i in range(0, len(registers_list))}
    init, instructions = instruction(tree)
    pprint(instructions)
    print("\nINIT VALUES: \n ", init)
    # print(registers)
    # print(tree)
    eval_expression(registers, instructions, init)
    exit()
    # test = "n0 R2 JMP N1b"
    # print(parser.parse(test))


main()
