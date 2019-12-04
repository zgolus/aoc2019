import collections

r = range(147981,691423)
# r = [111111, 223450, 123789, 112233, 123444, 111122]

valid = set()

def check_c1(n):
    s = str(n)
    c1 = True
    for i in range(len(s)):
        p = 0
        if i > 0:
            p = int(s[i-1])
        d = int(s[i])
        if d < p:
            c1 = False
    return c1

def check_c2(n):
    s = str(n)
    r = collections.defaultdict(int)
    for i in range(len(s)):
        d = int(s[i])
        r[d] = r[d] + 1 
    return len([x for x in r if r[x] > 1 and r[x] <= 2]) > 0 # part 2
    # return len([x for x in r if r[x] > 1]) > 0 # part 1

for n in r:
    if check_c1(n) and check_c2(n):
        valid.add(n)

print(len(valid))