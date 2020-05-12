n = int(input())

def solve(x, y, a, b):
	cost = 0
	if b > 2 * a:
		# use a
		cost = a * (x + y)
	else:
		# use b
		cost = b * min(x, y) + a * abs(x - y)
	return cost



for _ in range(n):
	x, y = list(map(int, input().split()))
	a, b = list(map(int, input().split()))
	print(solve(x, y, a, b))