from collections import defaultdict
orbits = defaultdict(list)
start = ''
end = ''

def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: 
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest

def parse_orbit_data(data):
    global orbits, start, end
    orbited, orbiting = data.split(")")
    orbits[orbited].append(orbiting)
    orbits[orbiting].append(orbited)
    if orbiting == 'YOU':
        start = orbited
    if orbiting == 'SAN':
        end = orbited

with open("day6/input.txt") as f:
    [parse_orbit_data(x.strip()) for x in f.readlines()]

print(find_path(orbits, start, end), len(find_path(orbits, start, end)) - 1)