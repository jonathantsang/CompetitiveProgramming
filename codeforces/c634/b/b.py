t = int(input())

def solve(n, a, b):
	ans = []
	c = 0
	for i in range(0, n):
		ans.append(chr(97+c))
		c += 1
		c %= b
	return "".join(ans)

for _ in range(0, t):
	n, a, b = list(map(int, input().split()))
	soln = solve(n, a, b)
	print(soln)