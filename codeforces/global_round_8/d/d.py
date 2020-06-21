from collections import defaultdict

rr = lambda: input()
rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

INF=float('inf')

def solve(N,A):
	arr = [0]*20
	for a in A:
		for i in range(20):
			if a&(1<<i):
				arr[i] += 1
	ans = 0
	for i in range(N):
		t = 0
		for j,a in enumerate(arr):
	    	if i < a:
	        	t += (1<<j)
		ans += t*t
	return ans

n = rri()
arr = rrm()
print(solve(n,arr))

# from prd_xxx
