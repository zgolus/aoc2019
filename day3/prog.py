from collections import defaultdict

with open('input.txt') as f:
    a, b = [x.strip().split(",") for x in f.readlines()]

def plot(source, name):
    x, y = 0, 0
    l = 0
    global grid
    global pedo
    for path in source:
        dir = path[0]
        steps = int(path[1:])
        for _ in range(steps):
            l = l + 1
            if dir == "R":
                x = x + 1
            if dir == "L":
                x = x - 1
            if dir == "U":
                y = y + 1
            if dir == "D":
                y = y - 1
            grid[(x, y)].add(name)
            pedo[(x, y)].add(l)

grid = defaultdict(set)
pedo = defaultdict(set)

plot(a, "a")
plot(b, "b")

crossings = []
lengths = []
for coord in grid:
    if len(grid[coord]) >= 2:
        crossings.append(coord)
        lengths.append(pedo[coord])

steps_combined = [sum(x) for x in lengths]
distances = [abs(x[0]) + abs(x[1]) for x in crossings]

print(f"Shortest distance: {sorted(distances)[0]}\nFewest steps: {sorted(steps_combined)[0]}")