# from collections import defaultdict

import io, os, math
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

rr = lambda: input()
rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

INF=float('inf')

def solve(N):
	if N==1:
		return 0
	
	moves = float('inf')
	for val in range(1,N+1):
		# increment, then paste rest
		takes = val-1 # increments
		print('orig',takes, N//val)
		takes += (N//val)-1

		moves = min(moves, takes)

	return moves


t = rri()
for _ in range(t):
	N=rri()
	print(solve(N))
