t = int(input())

def solve(n, k):
	final = 0
	s = 2 # smallest divisor of 2
	while n % s != 0:
		s += 1
	final += n + s + (k-1) * 2
	return final


for _ in range(t):
	n, k = list(map(int, input().split()))
	print(solve(n, k))
