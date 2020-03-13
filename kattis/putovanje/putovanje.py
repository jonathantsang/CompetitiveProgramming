n, c = list(map(int, input().split()))
vals = list(map(int, input().split()))

b = 0
for i in range(len(vals)):
    t = 0
    m = 0
    for j in range(i, len(vals)):
        if t + vals[j] <= c:
            t += vals[j]
            m += 1
    b = max(b, m)
print(b)
