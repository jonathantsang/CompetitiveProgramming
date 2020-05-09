n = int(input())

def solve(n):
	ans = []
	n = str(n)
	for i, d in enumerate(n):
		if d != '0':
			ans.append(d + "0" * (len(n) - i - 1))
	return ans


for _ in range(n):
	n = int(input())
	a = solve(n)
	print(str(len(a)))
	print(" ".join(a))