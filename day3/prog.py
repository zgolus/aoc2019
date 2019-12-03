from collections import defaultdict

with open('input.txt') as f:
    a, b = [x.strip().split(",") for x in f.readlines()]

# a = "R8,U5,L5,D3".split(",")
# b = "U7,R6,D4,L4".split(",")

# a = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51".split(",")
# b = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7".split(",")

# a = "R75,D30,R83,U83,L12,D49,R71,U7,L72".split(",")
# b = "U62,R66,U55,R34,D71,R55,D58,R83".split(",")

def plot(source, name):
    x, y = 0, 0
    global grid
    for path in source:
        dir = path[0]
        steps = int(path[1:])
        for _ in range(steps):
            if dir == "R":
                x = x + 1
            if dir == "L":
                x = x - 1
            if dir == "U":
                y = y + 1
            if dir == "D":
                y = y - 1
            grid[(x, y)].add(name)

grid = defaultdict(set)

plot(a, "a")
plot(b, "b")

crossings = []
for coord in grid:
    if len(grid[coord]) >= 2:
        crossings.append(coord)

distances = [abs(x[0]) + abs(x[1]) for x in crossings]

print(crossings, distances)

print(sorted(distances)[0])