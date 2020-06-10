from collections import Counter

t = int(input())

rr = lambda: input()
rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

def solve(N, arr):
	amt = 1
	newamt = 0
	arr.sort()
	i = 0
	count = Counter(arr)
	seen = set()
	for v in arr:
		if v in seen:
			continue
		seen.add(v)
		if amt + newamt + (count[v]-1) >= v: # minus 1 since can't see self
			amt += count[v] + newamt
			newamt = 0
		else:
			newamt += count[v]
	return amt

for _ in range(t):
	n = rri()
	arr = rrm()
	print(solve(n, arr))
