# from collections import defaultdict

import io, os, math
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

rr = lambda: input()
rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

INF=float('inf')

def solve(L,R):
	def lcm(a, b):
		return abs(a * b) // math.gcd(a, b)

	# L <= lcm(a,b) <= R
	for a in range(L, R):
		b = 2*a
		if b > R:
			break
		else:
			if L <= lcm(a,b) <= R:
				print(a,b)
				return
			else:
				break
	print(-1,-1)
	return

t = rri()
for _ in range(t):
	L,R=rrm()
	solve(L,R)
