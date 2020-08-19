# from collections import defaultdict

import io, os, math
#input = io.BytesIO(os.read(0,os.fstat(0).stsize)).readline

rr = lambda: input()
rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

INF=float('inf')

a = []

t = rri()
for  in range(t):
    t,d=rrm()
    a.append((t,d))

a.sort()
maxspeed = 0
N = len(a)
for i in range(1,N):
    dist = abs(a[i][1]-a[i-1][1])
    ti = a[i][0]-a[i-1][0]
    maxspeed=max(maxspeed, dist/ti)
print(maxspeed)
