# from collections import defaultdict

rr = lambda: input()
rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

INF=float('inf')
FIRST,SECOND="First","Second"

def solve(N,A):
	dp = [0 for _ in range(N)] # at pile i, who wins 0->first, 1->second
	dp[0] = 0
	larger = -1

	if A[0] > 1:
		larger = 0

	for i,v in enumerate(A):
		if i != 0: # skip first
			if larger != -1:
				dp[i] = dp[larger]
			else:
				dp[i] = dp[i-1]^1

			if larger == -1 and A[i] > 1:
				larger = i

	#print(A)
	#print(dp)
	return FIRST if dp[-1] == 0 else SECOND

t = rri()
for _ in range(t):
	N=rri()
	A=rrm()
	print(solve(N,A))
