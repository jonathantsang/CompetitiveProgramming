import sys

n = int(sys.stdin.readline())
names = {}
for _ in range(0, n):
    name = sys.stdin.readline().split('\n')[0]
    if name in names:
        names[name] += 1
    else:
        names[name] = 1
least = float('inf')
m = []
for name in names:
    if names[name] < least:
        m = [name]
        least = names[name]
    elif names[name] == least:
        m.append(name)

m.sort()
for name in m:
    print(name)
