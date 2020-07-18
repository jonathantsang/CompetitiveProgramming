# from collections import defaultdict

rr = lambda: input()
rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

INF=float('inf')

def solve(N,arr):
	# no dupes cause permutation
	ans = []
	seen = set()
	for v in arr:
		if v not in seen:
			seen.add(v)
			ans.append(v)
	return ' '.join(list(map(str, ans)))

t = rri()
for _ in range(t):
	n = rri()
	arr = rrm()
	print(solve(n, arr))
