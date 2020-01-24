import sys

def entire_interval(intervals, start, end):
    # want start to end
	intervals.sort()
	i = 0
	while(i < len(intervals)-1):
		if intervals[i][1] >= intervals[i+1][0]:
			intervals[i][1] = max(intervals[i][1], intervals[i+1][1])
			intervals.pop(i+1)
		else:
			i += 1
	if len(intervals) > 1 or intervals[0][0] > start or intervals[0][1] < end:
		return False
	else:
		return True
i = 0
nxnyw = []
nx = 0
ny = 0
w = 0
x_vals = []
y_vals = []
for line in sys.stdin:
	if line == "0 0 0.0":
		break
	if i == 0:
		nxnyw = list(map(float, line.split()))
		nx = nxnyw[0]
		ny = nxnyw[1]
		w = nxnyw[2]
	elif i == 1:
		x_vals = list(map(float, line.split()))
	elif i == 2:
		y_vals = list(map(float, line.split()))
		# perform lawnmower check
		# need x and y to span entire interval, otherwise fail
		x_intervals = []
		y_intervals = []
		for x in x_vals:
			x_intervals.append([x-w/2, x+w/2])
		for y in y_vals:
			y_intervals.append([y-w/2, y+w/2])
		if (entire_interval(x_intervals, 0, 75.0) and entire_interval(y_intervals, 0, 100.0)):
			print("YES")
		else:
			print("NO")
	if i == 2:
		i = 0
	else:
		i += 1
