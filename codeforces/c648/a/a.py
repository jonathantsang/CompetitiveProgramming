rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

t = rri()

def solve(N, M, grid):
	xpossible = set([i for i in range(M)]) # columns not having a 1
	ypossible = set([i for i in range(N)]) # rows not having a 1
	for i in range(N):
		for j in range(M):
			if grid[i][j] == 1:
				if i in ypossible:
					ypossible.remove(i)
				if j in xpossible:
					xpossible.remove(j)
	#print(xpossible, ypossible)
	# possible need 1 x and 1 y
	leng = min(len(xpossible), len(ypossible))
	if leng & 1:
		return "Ashish"
	else:
		return "Vivek"

for _ in range(t):
	n, m = rrm()
	arr = []
	for _ in range(n):
		arr.append(rrm())
	print(solve(n,m,arr))
