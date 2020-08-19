from collections import Counter, deque

import io, os, math
#input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

rr = lambda: input()
rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

INF=float('inf')

N=rr()
H=rr()

amt = 0
c = Counter(N)
hay = Counter(H[:len(N)])
w = deque(H[:len(N)])
lo = 0 # starts
hi = len(N)-1 # includes
seen = set()
while hi < len(H):
    #print(lo, hi, hay)
    if c == hay:
        seen.add(''.join(w))

    w.popleft()
    hay[H[lo]] -= 1 # remove previous
    if hay[H[lo]] == 0:
        del hay[H[lo]]

    hi+=1
    if hi == len(H):
        break
    hay[H[hi]] += 1
    w.append(H[hi])

    lo+=1

print(len(seen))
