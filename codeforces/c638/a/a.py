t = int(input())

def solve(n):
	p1 = 2**n
	p2 = 0
	for i in range(1, n//2):
		p1 += 2**i
	for i in range(n//2, n):
		p2 += 2**i
	#print(p1, p2)
	return abs(p1 - p2)

for _ in range(t):
	n = int(input())
	print(solve(n))