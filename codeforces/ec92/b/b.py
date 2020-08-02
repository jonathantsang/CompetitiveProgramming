from collections import defaultdict, deque
from functools import lru_cache

import io, os, math
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

rr = lambda: input()
rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

INF=float('inf')

def solve(N,K,Z,A):
	dp = defaultdict(int) # used moves, back used -> amt optimal
	dp[0][0] = A[0]
	for i in range(Z):
		dp[0][i] = A[0]

	best = 0
	for i in range(1,K):
		# move right normally
		dp[i] = max(dp[i], dp[i-1]+A[i])

		# move left and then right
		if i+2 >= K:
			best = max(dp[i], dp[i-1]+A[i-1]) # doesnt have enough moves to move back
		else:
			dp[i] = max(dp[i], dp[i-1]+A[i-1]+A[i])

	return max(best, dp[K-1])

t = rri()
for _ in range(t):
	N,K,Z=rrm()
	A=rrm()
	print(solve(N,K,Z,A))
