# from collections import defaultdict

rr = lambda: input()
rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

INF=float('inf')

def solve(n,arr):
	odd = 0
	even = 0
	mismatch = 0
	for i,v in enumerate(arr):
		if v&1:
			odd+=1
			if not i&1: # even i on odd num
				mismatch += 1
		else:
			even+=1
			if i&1: # odd i on even num
				mismatch += 1
	# for length n
	# n//2 even
	# n//2 odd
	wanteven = n//2+ +(n%2==0)
	wantodd = n//2
	if odd != wantodd and even != wanteven:
		return -1
	# differences in swaps needs to be even
	if mismatch&1:
		return -1
	return mismatch // 2

t = int(input())
for _ in range(t):
	n=rri()
	arr=rrm()
	print(solve(n,arr))
