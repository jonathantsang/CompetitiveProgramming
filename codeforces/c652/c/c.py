# from collections import defaultdict
import heapq

rr = lambda: input()
rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

INF=float('inf')

def solve(N,K,A,W):
	lo = 0
	hi = N-1
	A.sort() # two pointer for largest and smallest values
	W=sorted(W, reverse=True) # want 1 before 3

	total = 0

	ones = 0
	for c in W:
		if c == 1:
			ones += 1
	for _ in range(ones):
		total += A[hi] + A[hi]
		hi -= 1

	for count in W:
		if count == 1:
			break
		largest = 0
		smallest = 0

		if count == 1:
			largest = A[hi]
			smallest = A[hi]
			hi -= 1
		else:
			largest = A[hi]
			smallest = A[lo]
			hi -= 1
			lo += count-1
		#print('x', largest, smallest)

		total += largest + smallest

	return total

t = rri()
for _ in range(t):
	n,k=rrm()
	arr=rrm()
	w=rrm()
	print(solve(n,k,arr,w))
