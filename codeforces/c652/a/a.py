# from collections import defaultdict

rr = lambda: input()
rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

INF=float('inf')

def solve(n):
	if n %4 == 0:
		return "YES"
	return "NO"

t = rri()
for _ in range(t):
	n = rri()
	print(solve(n))
