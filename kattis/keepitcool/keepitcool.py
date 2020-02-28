n, m, s, d = list(map(int, input().split()))
slots = list(map(int, input().split()))
slots = [(slots[i], i) for i in range(0, len(slots))]
filled = ['0' for _ in range(0, len(slots))]

if sum(v[0] for v in slots) < m:
    print("impossible")
    exit(0)

slots.sort()
for i in range(0, len(slots)):
    sub = min(n, d - slots[i][0])
    n -= sub
    filled[slots[i][1]] = str(sub)
    if n <= 0:
        break

if n > 0:
    print("impossible")
    exit(0)

# cold
# keep i
for j in range(i+1, len(slots)):
    m -= slots[j][0]

if m > 0:
    print("impossible")
    exit(0)

print(" ".join(filled))
