n = int(input())

# int(input())
# list(map(int, input().split()))

def solve(n, m):
	# want want entire row of n lights, m lights, (and extra for odd #)
	# or entire row of n lights, m lights (and fill the last row or col horizontally/vertically)
	a = m * n//2 + n%2
	b = n * m//2 + m%2
	c = m * n//2 + m//2+m%2
	d = n * m//2 + n//2+n%2
	return min(a,b,c,d)

for _ in range(n):
	n, m = list(map(int, input().split()))
	print(solve(n, m))
