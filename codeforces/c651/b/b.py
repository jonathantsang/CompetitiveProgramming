# from collections import defaultdict

rr = lambda: input()
rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

INF=float('inf')
primes = None # set later on

def solve(N,A):
	# O(n^2)
	used = set()
	pairs = []
	for i in range(len(A)):
		if i in used:
			continue
		# search for same parity
		for j in range(len(A)):
			#print(A[i], A[j], i,j)
			if j not in used and i != j and A[i]&1 == A[j]&1:
				pairs.append((i,j))
				used.add(i)
				used.add(j)
				break
		if len(pairs) == N-1:
			#print("break")
			break

	#print(pairs)
	for i,j in pairs:
		print(i+1, j+1)

t = rri()
for _ in range(t):
	n=rri()
	arr=rrm()
	solve(n,arr)
