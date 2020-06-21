from collections import deque

rr = lambda: input()
rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

INF=float('inf')

def solve(N):
	print(1+3*(n+1))
	print(-1,-1)
	for i in range(n+1):
		print(i,i)
		print(i,i-1)
		print(i-1,i)

n = rri()
solve(n)

# from janwil
