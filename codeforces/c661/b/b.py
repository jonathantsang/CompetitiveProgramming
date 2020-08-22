# from collections import defaultdict

import io, os, math
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

rr = lambda: input()
rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

INF=float('inf')

def solve(N,A,B):
	targetA=min(A)
	targetB=min(B)
	ops = 0
	for ga,gb in zip(A,B):
		diffA=ga-targetA
		diffB=gb-targetB
		ops += max(diffA,diffB)
	return ops

t = rri()
for _ in range(t):
	N=rri()
	A=rrm()
	B=rrm()
	print(solve(N,A,B))
