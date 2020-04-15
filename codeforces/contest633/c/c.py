import math

t = int(input())

def solve(n,a):
    t = 0
    d = -float('inf')
    for i in range(0, len(a)):
        d = max(a[i], d)
        if d - a[i] > 0:
            j = 0
            now = d - a[i]
            while now > 0:
                now >>= 1
                j += 1

            t = max(j, t)
    return t

for _ in range(0, t):
    l = input() # length
    arr = list(map(int, input().split()))
    seconds = solve(l, arr)
    print(seconds)
