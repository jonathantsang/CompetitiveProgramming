from collections import defaultdict

rr = lambda: input()
rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

INF=float('inf')

def solve(N,K,A):
	diffs = defaultdict(int) # num % mod -> count (ideally want all 0)
	for v in A:
		diffs[v % K]+=1
	ops = 0
	#print(diffs)
	for remainder in diffs:
		if remainder == 0:
			continue
		ops = max(ops, K-remainder+K*(diffs[remainder]-1)+1)
	return ops

t = rri()
for _ in range(t):
	n,k=rrm()
	A=rrm()
	print(solve(n,k,A))
