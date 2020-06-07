t = int(input())

def solve(n, arr):
	dp = [1 for _ in range(n+1)] # best number of models at each point
	dp[0] = 0
	dp[1] = 1 # can always buy 1
	best = 1
	for i in range(1, n+1):
		# go to all numbers less than n divisible by j
		for k in range(i+i, n+1, i):
			if arr[k-1] > arr[i-1]:
				dp[k] = max(dp[i]+1, dp[k])
				best = max(dp[k], best)
		#print(dp)
	return best

for _ in range(t):
	n = int(input())
	arr = list(map(int, input().split()))
	print(solve(n, arr))