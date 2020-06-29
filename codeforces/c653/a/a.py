# from collections import defaultdict

rr = lambda: input()
rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

INF=float('inf')

def solve(X,Y,N):
	if N % X == Y:
		return N
	diff = N % X
	if diff > Y:
		return N - (diff-Y)
	else:
		return N - (diff) - (X-Y)

t = rri()
for _ in range(t):
	x,y,n=rrm()
	print(solve(x,y,n))
