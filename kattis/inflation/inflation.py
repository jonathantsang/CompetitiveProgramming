import sys

n = int(sys.stdin.readline())

cans = list(map(int, sys.stdin.readline().split()))
cans.sort()
possible = True
frac = float('inf')
for i in range(1, n+1):
    if cans[i-1] > i:
        possible = False
        break
    frac = min(frac, cans[i-1] / i)

if not possible:
    print("impossible")
else:
    print(frac)
