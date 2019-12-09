from typing import List
from collections import defaultdict
from itertools import permutations

def run(prog, input = False):
    cursor = 0
    input_index = 0
    while True:
        opcode = int(str(prog[cursor])[-2:])
        modes_str = str(prog[cursor])[:-2]
        i = 0
        modes = defaultdict(int)
        for mode in modes_str[::-1]:
            i = i + 1
            modes[i] = int(mode)
        if opcode == 99:
            break
        elif opcode == 1:
            param1 = prog[cursor + 1]
            param2 = prog[cursor + 2]
            param3 = prog[cursor + 3]
            if modes[1] == 0:
                param1 = prog[param1]
            if modes[2] == 0:
                param2 = prog[param2]
            prog[param3] = param1 + param2
            cursor = cursor + 4
        elif opcode == 2:
            param1 = prog[cursor + 1]
            param2 = prog[cursor + 2]
            param3 = prog[cursor + 3]
            if modes[1] == 0:
                param1 = prog[param1]
            if modes[2] == 0:
                param2 = prog[param2]
            prog[param3] = param1 * param2
            cursor = cursor + 4
        elif opcode == 3:
            if input:
                val = input[input_index]
                input_index += 1
            else:
                val = input()
            prog[prog[cursor + 1]] = int(val)
            cursor = cursor + 2
        elif opcode == 4:
            param1 = prog[cursor + 1]
            if modes[1] == 0:
                param1 = prog[param1]
            print(param1)
            return param1
            cursor = cursor + 2
        elif opcode == 5:
            param1 = prog[cursor + 1]
            if modes[1] == 0:
                param1 = prog[param1]
            param2 = prog[cursor + 2]
            if modes[2] == 0:
                param2 = prog[param2]
            if param1 != 0:
                cursor = param2
            else:
                cursor = cursor + 3
        elif opcode == 6:
            param1 = prog[cursor + 1]
            if modes[1] == 0:
                param1 = prog[param1]
            param2 = prog[cursor + 2]
            if modes[2] == 0:
                param2 = prog[param2]
            if param1 == 0:
                cursor = param2
            else:
                cursor = cursor + 3
        elif opcode == 7:
            param1 = prog[cursor + 1]
            if modes[1] == 0:
                param1 = prog[param1]
            param2 = prog[cursor + 2]
            if modes[2] == 0:
                param2 = prog[param2]
            param3 = prog[cursor + 3]
            if param1 < param2:
                prog[param3] = 1
            else:
                prog[param3] = 0
            cursor = cursor + 4
        elif opcode == 8:
            param1 = prog[cursor + 1]
            if modes[1] == 0:
                param1 = prog[param1]
            param2 = prog[cursor + 2]
            if modes[2] == 0:
                param2 = prog[param2]
            param3 = prog[cursor + 3]
            if param1 == param2:
                prog[param3] = 1
            else:
                prog[param3] = 0
            cursor = cursor + 4
        else:
            exit(opcode)
    return prog[0]


prog = [3,8,1001,8,10,8,105,1,0,0,21,38,63,80,105,118,199,280,361,442,99999,3,9,102,5,9,9,1001,9,3,9,1002,9,2,9,4,9,99,3,9,1001,9,4,9,102,4,9,9,101,4,9,9,102,2,9,9,101,2,9,9,4,9,99,3,9,1001,9,5,9,102,4,9,9,1001,9,4,9,4,9,99,3,9,101,3,9,9,1002,9,5,9,101,3,9,9,102,5,9,9,101,3,9,9,4,9,99,3,9,1002,9,2,9,1001,9,4,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,99]
# phases = [1,0,4,3,2]
input = 0

phases_list = list(permutations(range(5), 5))
outputs = {}

for phases in phases_list:
    input = 0
    for phase in phases:
        prog_copy = prog[:]
        output = run(prog_copy, [phase, input])
        input = output
    outputs[output] = phases

print(max(outputs))