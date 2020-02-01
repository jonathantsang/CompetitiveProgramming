import sys

n = int(sys.stdin.readline())

for i in range(0, n):
	line = sys.stdin.readline().split()
	npk = list(map(int, line))
	n = npk[0]
	p = npk[1]
	k = npk[2]

	line = sys.stdin.readline().split()
	items = list(map(int, line))

	items.sort()

	best = 0
	for i in range(0, len(items)):
		total = 0
		coins = p
		j = i
		while(j >= 0 and coins > 0):
			if items[j] > coins:
				pass
			else:
				coins -= items[j]
				total += 1
				# Unless it is index 0, get an extra one too
				if j != 0:
					total += 1
					j -= 1
			j -= 1
		best = max(best, total)
	print(best)
