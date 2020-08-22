# from collections import defaultdict

import io, os, math
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
# WARNING
# this turns binary strings ex. "0011" to ints by default
# making rr(), read impossible as a string

rr = lambda: input()
rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

INF=float('inf')

def solve(N,S,E):
	pass

t = rri()
for _ in range(t):
	N,S=rrm()
	E = defaultdict(list) # vertice -> [(vertice adj, weight)]
	for _ in range(N):
		v,u,w=rrm()
		E[v].append((u,w))
		E[u].append((v,w))

	print(solve(N,S,E))
