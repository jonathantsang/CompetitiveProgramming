import sys

n = int(sys.stdin.readline())
total = 0
for line in sys.stdin:
	qy = line.split()
	q = float(qy[0])
	y = float(qy[1])
	total += q * y
print(total)