# from collections import defaultdict

rr = lambda: input()
rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

INF=float('inf')

def solve(a,b,n):
	ops = 0
	while a <= n and b <= n:
		#print(a,b,ops)
		if a < b:
			a += b
		else:
			b += a
		ops += 1
	return ops

t = int(input())
for _ in range(t):
	a,b,n=rrm()
	print(solve(a,b,n))
