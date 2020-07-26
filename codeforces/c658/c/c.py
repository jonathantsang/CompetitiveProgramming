# from collections import defaultdict

rr = lambda: input()
rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

INF=float('inf')

def verify(steps, A,B):
	print("verify")
	for j, s in enumerate(steps):
		s = int(s)
		a = A[:s]
		for i in range(s):
			a[i] ^= 1
		a = a[::-1]
		for i in range(s):
			A[i] = a[i]
		#print(A, "step", j, s)
	for v1,v2 in zip(A,B):
		if v1 != v2:
			return False
	return True

def solve(N,A,B):
	if A == B:
		print(0)
		return
	# at most 3n operations
	A = list(map(int, list(A)))
	B = list(map(int, list(B)))
	C = A.copy()

	# operation, flips all bits and reverses
	lo = 0 # lo is always 0
	hi = len(A)-1

	steps = []
	while lo <= hi:
		if A[hi] == B[hi]:
			# nothing, no flips
			pass
		else:
			steps.append(str(hi+1))
			steps.append(str(lo+1))
			steps.append(str(hi+1))
			# A[hi] should be fixed to B[hi], 3 flips
		hi -= 1
	# verify
	#print(verify(steps,C,B))

	print(len(steps,), ' '.join(steps))

t = rri()
for _ in range(t):
	N=rri()
	A=rr()
	B=rr()
	solve(N,A,B)
