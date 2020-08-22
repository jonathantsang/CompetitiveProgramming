from collections import Counter

import io, os, math
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

rr = lambda: input()
rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

INF=float('inf')

def solve(N,A):
	best = 0
	for weight in range(1,101): # max w is 50, so 50+50
		c = Counter(A)
		boats = 0
		for v in A:
			if v == weight-v and c[v] == 1: # only one, cannot do it
				continue
			if weight-v in c and c[weight-v] > 0 and c[v] > 0:
				c[weight-v]-=1
				c[v]-=1
				boats += 1
		best = max(boats, best)
	return best

t = rri()
for _ in range(t):
	N=rri()
	A=rrm()
	print(solve(N,A))
