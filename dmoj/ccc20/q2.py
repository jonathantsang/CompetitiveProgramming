from collections import deque

import io, os, math
#input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

rr = lambda: input()
rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

INF=float('inf')

grid = []

M=rri()
N=rri()

for i in range(M):
    row = rrm()
    grid.append(row)

seen = set()
q = deque([(0,0)])

while q:
    #print(q)
    y,x = q.popleft()

    if (y,x) in seen:
        continue
    seen.add((y,x))

    if y == M-1 and x == N-1:
        break

    possible = []
    for i in range(M):
        if (grid[y][x]) % (i+1) == 0 and (grid[y][x])//(i+1)-1 < N:
            #print(i, M//(i+1)-1)
            q.append((i,(grid[y][x])//(i+1)-1))

    if y == M-1 and x == N-1:
        break

print("yes" if (M-1,N-1) in seen else "no")
