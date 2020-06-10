t = int(input())

rr = lambda: input()
rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

def solve(n,m,x,y,grid):
	cost = 0
	for i in range(n):
		dp = [0] * (m+1)
		for j in range(m):
			# need to colour
			if grid[i][j] == '.':
				dp[j+1] = dp[j]+x
				if j >= 1 and grid[i][j-1] == '.':
					dp[j+1] = min(dp[j-1]+y, dp[j+1])
			else:
				# don't need to colour
				dp[j+1] = dp[j]
		cost += dp[-1]
		#print(dp)
	return cost

for _ in range(t):
	n,m,x,y = rrm()
	grid = []
	for _ in range(n):
		grid.append(list(rr()))
	print(solve(n,m,x,y,grid))
