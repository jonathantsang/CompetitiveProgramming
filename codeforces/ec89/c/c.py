# import deque, defaultdict from collections
from collections import defaultdict

t = int(input())

rr = lambda: input()
rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

def solve(N,M,grid):
	#print(grid)
	start = set([(0,0)])
	end = set([(N-1,M-1)])

	valid = True
	changes = 0
	allstart = set() # all seen
	allend = set() # all seen
	while valid:
		startcount = defaultdict(int)
		endcount = defaultdict(int)
		for y,x in start:
			startcount[grid[y][x]]+=1
		for y,x in end:
			#print(y,x)
			endcount[grid[y][x]]+=1
		#print(startcount, endcount)
		#print("changes ", changes)
		# convert to all 1 or convert to all 0
		changes+=min(startcount[0]+endcount[0],
						startcount[1]+endcount[1])

		newstart = set()
		# add adjacent cells
		for y,x in start:
			for iy,ix in [(1,0),(0,1)]:
				iy+=y
				ix+=x
				if 0 <= ix < M and 0 <= iy < N:
					newstart.add((iy, ix))
					allstart.add((iy, ix))
		newend = set()
		for y,x in end:
			for iy,ix in [(-1,0),(0,-1)]:
				iy+=y
				ix+=x
				if 0 <= ix < M and 0 <= iy < N:
					newend.add((iy, ix))
					allend.add((iy, ix))

		start = newstart
		end = newend
		#print(start, end)
		if len(allstart & allend) > 0:
			# overlap
			valid = False
			break

	return changes

for _ in range(t):
	n,m=rrm()
	grid = []
	for _ in range(n):
		grid.append(rrm())
	print(solve(n,m,grid))
