t = int(input())

def solve(n):
	if n == 1:
		return 0
	amt = 0
	outrow = 8
	j = 1
	for i in range(1, n, 2):
		#print(i, j)
		amt += j * outrow
		outrow += 8
		j += 1
	return amt

for _ in range(t):
	n = int(input())
	print(solve(n))