from collections import deque

t = int(input())

INF=float('inf')

rr = lambda: input()
rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

def solve(N,x,arr):
	best = 0

	sumsofar = 0
	for i in range(N):
		sumsofar += arr[i]
		if sumsofar % x != 0:
			best = max(best, i+1)
	sumsofar = 0
	for i in range(N-1, -1, -1):
		sumsofar += arr[i]
		if sumsofar % x != 0:
			best = max(best, (N-1-i)+1)

	if best == 0:
		return -1
	return best

for _ in range(t):
	n,x=rrm()
	arr=rrm()
	print(solve(n,x,arr))
