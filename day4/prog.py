r = range(147981,691423)
# r = [123456, 12343, 12534, 12245, 111111, 223450, 123789]

valid = set()

for n in r:
    s = str(n)
    p = 0
    c1 = True
    c2 = False
    for j in range(len(s)):
        p = 0
        if j > 0:
            p = int(s[j-1])
        d = int(s[j])
        if d < p:
            c1 = False
        if d == p:
            c2 = True
    
    if c1 and c2:
        valid.add(n)

print(len(valid))