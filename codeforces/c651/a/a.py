# from collections import defaultdict

rr = lambda: input()
rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

INF=float('inf')

def solve(n):
	return n//2


t = rri()
for _ in range(t):
	n=rri()
	print(solve(n))
