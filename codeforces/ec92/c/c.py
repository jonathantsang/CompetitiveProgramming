from collections import defaultdict

rr = lambda: input()
rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

INF=float('inf')

def solve(S):
	if len(S) == 2:
		return S
	# need even count of chars
	count = Counter(S)
	a = []
	for c in S:
		if count[c] == 1:

t = rri()
for _ in range(t):
	S=rr()
	print(solve(S))
