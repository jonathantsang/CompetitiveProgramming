t = int(input())

# int(input())
# list(map(int, input().split()))

def solve(n, grid):
	for i in range(n-2, -1, -1):
		for j in range(n-2, -1, -1):
			if grid[i][j] == '1' and (grid[i+1][j] != '1' and grid[i][j+1] != '1'):
				return False
	return True

for _ in range(t):
	n = int(input())
	grid = []
	for _ in range(n):
		grid.append(list(input()))
	a = solve(n,grid)
	if a == True:
		print("YES")
	else:
		print("NO")
