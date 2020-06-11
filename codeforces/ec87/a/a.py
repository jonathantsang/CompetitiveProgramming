n = int(input())

INF=float('inf')

rr = lambda: input()
rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

def solve(a,b,c,d):
	need = a - b
	if need <= 0:
		return b
	if c <= d:
		return -1
	return b + c * (need//(c-d)+ +(need%(c-d)!=0))

for _ in range(n):
	a,b,c,d=rrm()
	print(solve(a,b,c,d))
