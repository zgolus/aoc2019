from collections import defaultdict

orbits = defaultdict(list)

def parse_orbit_data(data: str):
    global orbits
    orbited, orbiting = data.split(")")
    orbits[orbiting].append(orbited)
    indirect = orbits[orbited]
    orbits[orbiting].extend(indirect)
    [orbits[x].extend(indirect + [orbited]) for x, y in orbits.items() if orbiting in y]

with open("day6/input.txt") as f:
    [parse_orbit_data(x.strip()) for x in f.readlines()]

cnt = 0
for o in orbits:
    cnt = cnt + len(orbits[o])

print(cnt)