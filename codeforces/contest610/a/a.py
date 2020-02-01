import sys

n = int(sys.stdin.readline())

for i in range(0, n):
	line = sys.stdin.readline().split()
	sebr = list(map(int, line))
	start = sebr[0]
	end = sebr[1]
	b = sebr[2]
	r = sebr[3]

	if start > end:
		start, end = end, start

	radius_start = b - r
	radius_end = b + r

	total = abs(end - start)

	# outside
	if radius_end < start or radius_start > end:
		print(total)
		continue

	# pure middle
	if radius_end <= end and radius_start >= start:
		total -= (radius_end - radius_start)
		print(total)
		continue

	# whole segment
	if radius_end >= end and radius_start <= start:
		total = 0
		print(total)
		continue
	
	# left
	if radius_end >= start and radius_start <= start:
		start = radius_end
		total = abs(end - start)
		print(total)
		continue

	# right
	if radius_start <= end and radius_end >= end:
		end = radius_start
		total = abs(end - start)
		print(total)
		continue



