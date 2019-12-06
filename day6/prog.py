from collections import defaultdict

orbits = defaultdict(list)

def parse_orbit_data(data: str):
    global orbits
    orbited, orbiting = data.split(")")
    orbits[orbiting].append(orbited)
    indirect = orbits[orbited]
    orbits[orbiting].extend(indirect)

with open("day6/input_test.txt") as f:
    [parse_orbit_data(x.strip()) for x in f.readlines()]

cnt = 0
for o in orbits:
    cnt = cnt + len(orbits[o])

print(cnt, orbits)

# COM)B
# B)C
# C)D
# D)E
# E)F
# B)G
# G)H
# D)I
# E)J
# J)K
# K)L
#         G - H       J - K - L
#        /           /
# COM - B - C - D - E - F
#                \
#                 I
