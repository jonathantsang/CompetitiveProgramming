from collections import deque

rr = lambda: input()
rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

INF=float('inf')

def solve(N,K,arr):
	left = [None] * n
	right = [None] * n

	f = INF
	for i in range(n):
		if arr[i] == '1':
			f = 0
		else:
			f += 1
		left[i] = f

	f = INF
	for i in range(n - 1, -1, -1):
		if arr[i] == '1':
			f = 0
		else:
			f += 1
		right[i] = f
	#print(left ,right)

	dp = [0 for _ in range(n)]
	dp[0] = 1 if min(left[i], right[i]) > K else 0
	amt = 0
	for i in range(1,n):
		if min(left[i], right[i]) > K and i-K-1>=0:
			dp[i] = max(dp[-1], dp[i-K-1]+1)
		else:
			dp[i] = dp[i-1]
	#print(dp)

	return dp[-1]

t = int(input())
for _ in range(t):
	n,k=rrm()
	arr=list(input())
	print(solve(n,k,arr))
