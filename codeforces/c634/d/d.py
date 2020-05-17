t = int(input())

def solve(g):
	g[0][0] = 1 if g[0][0] != 1 else 2
	g[1][4] = 1 if g[1][4] != 1 else 2
	g[2][8] = 1 if g[2][8] != 1 else 2
	g[3][7] = 1 if g[3][7] != 1 else 2
	g[4][1] = 1 if g[4][1] != 1 else 2
	g[5][3] = 1 if g[5][3] != 1 else 2
	g[6][6] = 1 if g[6][6] != 1 else 2
	g[7][2] = 1 if g[7][2] != 1 else 2
	g[8][5] = 1 if g[8][5] != 1 else 2
	return grid

def checkAnti(g):
	for r in grid:
		fine = False
		seen = set()
		for d in r:
			if d in seen:
				fine = True
				break
			else:
				seen.add(d)
	if not fine:
		print("BAD")
	for c in range(0, len(grid[0])):
		fine = False
		seen = set()
		for r in grid:
			if r[c] in seen:
				fine = True
				break
			else:
				seen.add(r[c])
	if not fine:
		print("BAD")

	for n in range(0, 9):
		for j in [[0,1,2], [3,4,5], [6,7,8]]:
			for i in [[0,1,2], [3,4,5], [6,7,8]]:
				fine = False
				seen = set()
				for jx in j:
					for ix in i: 
						if grid[jx][ix] in seen:
							fine = True
							break
						else:
							seen.add(grid[jx][ix])
	if not fine:
		print("BAD")
	#print("FINE")

for _ in range(0, t):
	grid = []
	for _ in range(0, 9):
		grid.append(list(map(int, list(str(input())))))
	#print(grid)
	a = solve(grid)
	#checkAnti(grid)
	for l in grid:
		print("".join(list(map(str, l))))