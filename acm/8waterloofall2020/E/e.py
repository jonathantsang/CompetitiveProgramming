from collections import defaultdict, deque

rr = lambda: input()
rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

INF=float('inf')

def solve(N,M,sidewalks):
	edges = defaultdict(list) # area -> list of areas

	for t,f in sidewalks:
		edges[t].append(f)
		edges[f].append(t)

	


N,M=rrm()
sidewalks = []
for _ in range(M):
	A,B=rrm()
	sidewalks.append((A,B))
solve(N,M,sidewalks)
