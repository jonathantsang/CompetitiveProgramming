# from collections import defaultdict

rr = lambda: input()
rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

INF=float('inf')

def solve(N):
	if N == 1:
		return 0
	twos=0
	threes=0
	while N % 2 == 0:
		N //= 2
		twos+=1
	while N % 3 == 0:
		N //= 3
		threes+=1
	# can add *2 anywhere
	if N == 1 and threes>0 and threes>=twos:
		return threes+threes-twos
	else:
		return -1

t = rri()
for _ in range(t):
	n = rri()
	print(solve(n))
