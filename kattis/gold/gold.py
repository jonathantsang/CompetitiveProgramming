import sys
import collections

w, h = list(map(int, sys.stdin.readline().split()))
grid = []
valid = [[-1 for _ in range(0, w)] for _ in range(0, h)]

px = -1
py = -1
y = 0
for line in sys.stdin.readlines():
    grid.append(list(line))
    if 'P' in grid[-1]:
        px = grid[-1].index('P')
        py = y
    y += 1

gold = 0
q = collections.deque()
q.append((px, py))

TRAP = 'T'
GOLD = 'G'
WALL = '#'

visited = set()

while len(q):
	x, y = q.popleft()
	if (x, y) in visited:
		continue
	visited.add((x, y))
	if grid[y][x] == GOLD:
		gold += 1
	if grid[y][x] == WALL:
		continue
	if grid[y-1][x] != TRAP and grid[y+1][x] != TRAP and grid[y][x-1] != TRAP and grid[y][x+1] != TRAP:
		q.append((x, y-1))
		q.append((x, y+1))
		q.append((x-1, y))
		q.append((x+1, y))

print(gold)
