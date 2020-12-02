# from collections import defaultdict

import io, os, math
#input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
# WARNING
# this turns binary strings ex. "0011" to ints by default
# making rr(), read impossible as a string

rr = lambda: input()
rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

INF=float('inf')

def solve(nums):
	m=set()
	N=len(nums)
	for i in range(N):
		for j in range(i+1,N):
			for k in range(j+1,N):
				if nums[i]+nums[j]+nums[k] == 2020:
					return nums[i]*nums[j]*nums[k]
	return 0

t = 1
for _ in range(t):
	ans = []
	a = rri()
	while a != '':
		ans.append(a)
		try:
			a=rri()
		except:
			break
	print(solve(ans))
