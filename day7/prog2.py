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
            output = param1
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
    return output


prog = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
input = 0

# phases_list = list(permutations(range(5), 5))
phases_list = [(9,8,7,6,5)]
outputs = {}

for phases in phases_list:
    prog_copy = prog[:]
    for phase in phases:
        output = run(prog_copy, [phase, input])
        input = output
    outputs[output] = phases

print(max(outputs))