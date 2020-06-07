t = int(input())

rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

def solve(a, K):
	for i in range(1,K):
		x=str(a)
		if '0' in x:
			break
		ma=max(x)
		mi=min(x)
		a+=int(ma)*int(mi)
	return a

for _ in range(t):
	a, K = rrm()
	print(solve(a, K))
