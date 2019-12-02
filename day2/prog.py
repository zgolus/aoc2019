import re
from typing import List

input = '1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,6,19,23,2,23,6,27,1,5,27,31,1,31,9,35,2,10,35,39,1,5,39,43,2,43,10,47,1,47,6,51,2,51,6,55,2,55,13,59,2,6,59,63,1,63,5,67,1,6,67,71,2,71,9,75,1,6,75,79,2,13,79,83,1,9,83,87,1,87,13,91,2,91,10,95,1,6,95,99,1,99,13,103,1,13,103,107,2,107,10,111,1,9,111,115,1,115,10,119,1,5,119,123,1,6,123,127,1,10,127,131,1,2,131,135,1,135,10,0,99,2,14,0,0'
# input = '1,1,1,4,99,5,6,0,99'

i = 0
input: List[int] = [int(x) for x in input.split(',')]
cursor = 0

# 12 2 8017076
# 13 2 8631476
# 14 2 9245876
# xx x 19690720
# 31 46 19690720

input[1] = 31
input[2] = 46

print(f"{100 * 31 + 46}")

while True:
    opcode = input[cursor]
    if opcode == 99:
        break
    in1 = input[cursor + 1]
    in2 = input[cursor + 2]
    out = input[cursor + 3]
    cursor = cursor + 4

    if opcode == 1:
        input[out] = input[in1] + input[in2]
    elif opcode == 2:
        input[out] = input[in1] * input[in2]
    else:
        exit(opcode)

print(input)