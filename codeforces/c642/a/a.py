t = int(input())

def solve(n, m):
	# want alternating 0s
	# 0 val 0 val etc.
	amt = 0

	if n == 1:
		return 0
	if n == 2:
		return m

	return m*2

for _ in range(t):
	n, m = list(map(int, input().split()))
	print(solve(n, m))