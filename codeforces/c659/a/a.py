# from collections import defaultdict

rr = lambda: input()
rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

INF=float('inf')
YES, NO="YES", "NO"
FIRST,SECOND="FIRST","SECOND"

def solve(N,A):
	maxlen = 52
	prev = 'a' * maxlen
	print(prev)
	for v in A:
		garbage = chr((ord(prev[v])-ord('a')+1)%26+ord('a'))
		cur = prev[:v] + garbage * (maxlen-v)
		print(cur)
		prev = cur


t = rri()
for _ in range(t):
	N=rri()
	A=rrm()
	solve(N,A)
