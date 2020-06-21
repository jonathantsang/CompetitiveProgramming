# from collections import defaultdict

rr = lambda: input()
rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

INF=float('inf')

def solve(b):
	ans = [b[0]]
	for i in range(1,len(b)-1,2):
		ans.append(b[i])
	ans.append(b[-1])
	return "".join(ans)

t = int(input())
for _ in range(t):
	b=rr()
	print(solve(b))
