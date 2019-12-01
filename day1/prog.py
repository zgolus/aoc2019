import math

tfn = 0

def fuel_needed(weight):
    global tfn
    fn = math.floor(weight / 3) - 2
    if fn >=0:
        tfn = tfn + fn
        fuel_needed(fn)

modules = []
with open('input.txt') as f:
    [fuel_needed(int(x.strip())) for x in f.readlines()]

print(tfn)