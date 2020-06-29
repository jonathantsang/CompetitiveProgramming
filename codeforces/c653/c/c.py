# from collections import defaultdict

rr = lambda: input()
rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

INF=float('inf')

def solve(N,S):
	invalid = 0
	bal = 0
	for b in S:
		if b == ')':
			bal -= 1
			if bal < 0:
				bal = 0
				invalid += 1
		else:
			bal += 1
	# balance at end is something

	return invalid


t = rri()
for _ in range(t):
	n = rri()
	s = rr()
	print(solve(n,s))
