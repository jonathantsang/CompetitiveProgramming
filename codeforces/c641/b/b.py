t = int(input())

def solve(n, arr):
	dp = [1 for _ in range(n+1)] # best number of models at each point
	dp[0] = 0
	dp[1] = 1 # can always buy 1
	for i in range(2, n+1):
		# use 1 and/or enumerate out
		j = i
		prev = 1
		running = 1
		while j < n+1:
			#print(prev, j)
			if arr[prev-1] < arr[j-1]:
				running += 1
			else:
				# larger so restart the sequence if not 1
				if prev != 1:
					break
			dp[j] = max(running, dp[j])
			prev = j
			j += j
		#print(dp)
	return max(dp)


for _ in range(t):
	n = int(input())
	arr = list(map(int, input().split()))
	print(solve(n, arr))