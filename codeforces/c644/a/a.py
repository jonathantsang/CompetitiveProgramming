n = int(input())

def solve(a, b):
	return min((max(2*a,b))**2, max(2*b, a)**2)

for _ in range(n):
	a, b = list(map(int, input().split()))
	print(solve(a, b))
