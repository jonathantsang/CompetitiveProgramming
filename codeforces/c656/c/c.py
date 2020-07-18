# from collections import defaultdict

rr = lambda: input()
rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

INF=float('inf')

def solve(N,A):
	end = N-1
	# decreasing
	for i in range(N-2,-1,-1):
		if A[i] < A[i+1]:
			break
		end = i
	#print(A)
	#print(end)

	for i in range(end-1, -1, -1):
		if A[i] > A[i+1]:
			return i+1 # prefix length

	return 0

t = rri()
for _ in range(t):
	n = rri()
	arr = rrm()
	print(solve(n,arr))
