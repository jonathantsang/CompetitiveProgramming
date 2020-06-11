#from collections import defaultdict

INF = float('inf')

t = int(input())

rr = lambda: input()
rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

def solve(n,x,m,ops):
	#print(ops)
	best = 1
	lo, hi = x,x # bounds for including k in it
	for s,f in ops:
		if (s <= x <= f) or (lo <= s <= hi) or (lo <= f <= hi):
			lo = min(lo, s)
			hi = max(hi, f)
			best = max(hi-lo+1, best)
	#print(lo,hi)
	return best


for _ in range(t):
	n,x,m=rrm()
	ops=[]
	for _ in range(m):
		ops.append(rrm())
	print(solve(n,x,m,ops))
