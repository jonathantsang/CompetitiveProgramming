# from collections import defaultdict

import io, os, math
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
# WARNING
# this turns binary strings ex. "0011" to ints by default
# making rr(), read impossible as a string

rr = lambda: input()
rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

INF=float('inf')

def solve(N,X):
	if N==1 or N==2:
		return 1
	lo,hi=3,X+2
	
	floor = 2
	while True:
		#print(lo,hi,N)
		if lo<=N<=hi:
			return floor
		floor+=1
		lo=hi+1
		hi=lo+(X-1)

	return -1

t = rri()
for _ in range(t):
	N,X=rrm()
	print(solve(N,X))
