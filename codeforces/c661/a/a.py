from collections import Counter

import io, os, math
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

rr = lambda: input()
rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

INF=float('inf')

def solve(N,A):
	s = Counter(A) # get rid of duplicates
	if len(s) == 1:
		return "YES"
	last = max(A)

	for v in sorted(list(s)):
		if v == last:
			# fine
			break
		if v+1 not in s:
			return "NO"
	return "YES"

t = rri()
for _ in range(t):
	N=rri()
	A=rrm()
	print(solve(N,A))
