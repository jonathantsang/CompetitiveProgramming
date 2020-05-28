t = int(input())

# int(input())
# list(map(int, input().split()))

def solve(n, k):
	if k >= n:
		return 1
	factors = []
	for d in range(1, int(n ** 0.5) + 1):
		if n % d == 0:
			factors.append(d)
			factors.append(n // d)
	factors.sort(reverse = True)
	for d in factors:
		if d <= k:
			return n // d

for _ in range(t):
	n, k = list(map(int, input().split()))
	print(solve(n,k))
