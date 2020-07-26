# from collections import defaultdict

rr = lambda: input()
rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

INF=float('inf')
YES, NO="YES", "NO"


def solve(N,M,A,B):
	C = set(A) & set(B)
	if len(C) > 0:
		print(YES)
		first = -1
		for v in C:
			first = v
			break
		print(1, first)
	else:
		print(NO)

t = rri()
for _ in range(t):
	N,M=rrm()
	A=rrm()
	B=rrm()
	solve(N,M,A,B)
