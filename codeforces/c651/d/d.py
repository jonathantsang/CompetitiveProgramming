# from collections import defaultdict

rr = lambda: input()
rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

INF=float('inf')

def check(val, cur, A):
	ans = 0
	for v in A:
		if cur:
			ans += 1
			cur ^= 1
		else:
			if v <= val: # keep min
				ans += 1
				cur ^= 1
	return ans >= k

def solve(N,K,A):
	lo,hi = 1,10**9
	while lo <= hi:
		mid = lo+hi >> 1
		if check(mid, 0, A) or check(mid, 1, A):
			hi = mid - 1
		else:
			lo = mid + 1
	return lo

n, k =rrm()
arr=rrm()
print(solve(n,k,arr))
