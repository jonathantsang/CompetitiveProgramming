n = int(input())
vals = list(map(int, input().split()))

seen = {}
for v in vals:
    if v in seen:
        seen[v] += 1
    else:
        seen[v] = 1

minval = 0
times = float('inf')
for v in seen:
    if seen[v] == 1:
        minval = max(minval, v)
        times = 1

if times == float('inf'):
    print("none")
else:
    print(vals.index(minval)+1)
