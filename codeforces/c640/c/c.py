t = int(input())

def solve(n, k):
	# how many multiples less than current
	ith = k - k // n

	# want to move from ith to kth
	diff = k - ith
	num = k

	while diff > 0:
		num += diff
		ith = num - num // n
		diff = k - ith
	return num

for _ in range(t):
	n, k = list(map(int, input().split()))
	print(solve(n, k))