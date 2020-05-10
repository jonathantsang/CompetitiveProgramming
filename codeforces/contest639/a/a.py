t = int(input())

def solve(n, m):
	pieces = n * m
	if n == 1 or m == 1:
		return "YES"
	elif n == 2 and m == 2:
		return "YES"
	else: # n and m > 2
		return "NO"

for _ in range(t):
	n, m = list(map(int, input().split()))
	print(solve(n, m))