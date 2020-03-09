n, p = list(map(int, input().split()))
vals = list(map(int, input().split()))

if p == 100:
    print("impossible")
    exit(0)

total = sum(vals)
avg = total / n
added = 0
while avg < p:
    total += 100
    n += 1
    added += 1
    avg = total / n
print(added)
