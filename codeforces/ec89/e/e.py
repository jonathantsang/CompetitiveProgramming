n = int(input())

rr = lambda: input()
rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

MOD = 998244353

def solve(n,m,a,b):
	dp = [0 for _ in range(len(b))]
	for i in range(len(b)):
		for j in range(len(a)):
			dp[i]


n,m=rrm()
a=rrm()
b=rrm()
print(solve(n,m,a,b))
