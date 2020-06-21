from collections import deque

rr = lambda: input()
rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

INF=float('inf')

def calc(ans):
	amt = 0
	prev = 1
	for i in range(len(ans)-1, -1, -1):
		prev *= ans[i]
	return prev

def solve(k):
	amt = 1
	chars = list("codeforces")
	ans = [1 for _ in range(len(chars))] # number of chars at each position in chars
	idx = len(chars)-1
	while calc(ans) < k:
		ans[idx] += 1
		if idx == -1:
			idx=len(chars)-1
		idx-=1

	ret = []
	for i,n in enumerate(ans):
		ret.append(chars[i]*n)
	return "".join(ret)

k=rri()
print(solve(k))
