import collections

t = int(input())

def solve(n, a):
	ht = collections.defaultdict(int)
	for s in a:
		ht[s] += 1
	unique = len(ht)
	max_same = max(ht.values())
	return max(min(unique, max_same-1), min(unique-1, max_same))

for _ in range(0, t):
	n = int(input())
	arr = list(map(int, input().split()))
	soln = solve(n, arr)
	print(soln)