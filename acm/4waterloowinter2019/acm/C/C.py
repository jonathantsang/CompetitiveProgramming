import sys

def dist(incident, guard):
	y = int(incident[1]) - guard[1]
	x = int(incident[0]) - guard[0]
	return pow(y, 2) + pow(x, 2)

gi = sys.stdin.readline().split()
g = int(gi[0])
inc = int(gi[1])
guards = []

for i in range(0, g):
	r = sys.stdin.readline().split()
	guards.append([int(r[0]), int(r[1])])

for i in range(0, inc):
	incident = sys.stdin.readline().split()
	bestdist = float('inf')
	beststeps = float('inf')
	# print(incident)
	for guard in guards:
		d = dist(incident, guard)
		if bestdist > d:
			bestdist = d
			y = abs(int(incident[1]) - guard[1])
			x = abs(int(incident[0]) - guard[0])
			beststeps = min(y, x) + max(y, x) - min(y, x)
	print(beststeps)