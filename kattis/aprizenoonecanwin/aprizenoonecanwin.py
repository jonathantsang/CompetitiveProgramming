n, x = list(map(int, input().split()))
vals = list(map(int, input().split()))

if n == 1:
    print(1)
    exit(0)

vals.sort()
res = 1
for i in range(1, len(vals)):
    if vals[i] + vals[i-1] <= x:
        res = i+1

print(res)
