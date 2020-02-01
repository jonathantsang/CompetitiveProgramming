import sys

def traverse(x, y, grid, path):
	if x == 0 and y == 0:
		return path
	if x < 0 or y < 0 or x >= len(grid) or y >= len(grid):
		return False
	if grid[y][x] == 'u':
		# Only can go up
		a = traverse(x, y-1, grid, "S" + path)
		if a != False:
			return a
	elif grid[y][x] == 'l':
		# Only can go left
		a = traverse(x-1, y, grid, "E" + path)
		if a != False:
			return a
	else:
		# Go left or up
		a = traverse(x, y-1, grid, "S" + path)
		if a != False:
			return a
		b = traverse(x-1, y, grid, "E" + path)
		if b != False:
			return b
	return False

n = int(sys.stdin.readline())
sys.setrecursionlimit(2500)
for t in range(1, n+1):
	dimension = int(sys.stdin.readline().split('\n')[0])
	lydia = sys.stdin.readline().split('\n')[0] ## Get rid of newline
	grid = [['a' for i in range(0, dimension)] for y in range(0, dimension)]
	for v in range(0, len(grid[0])):
		grid[0][v] = 'l'
	for v in range(0, len(grid)):
		grid[v][0] = 'u'
	xl = 0
	yl = 0
	for c in lydia:
		if c == 'S':
			grid[yl+1][xl] = 'l'
			yl += 1
		else:
			grid[yl][xl+1] = 'u'
			xl += 1
	path = traverse(dimension-1, dimension-1, grid, "")

	print("Case #" + str(t) + ": " + path)
