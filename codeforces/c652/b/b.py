# from collections import defaultdict

rr = lambda: input()
rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

INF=float('inf')

def solve(N, S):
	i = 0
	ans = []

	while i < len(S):
		if S[i] == '1':
			ones = 0
			zeroes = 0
			while i < len(S) and S[i] == '1':
				ones += 1
				i += 1
			while i < len(S) and S[i] == '0':
				zeroes += 1
				i += 1
			if ones > 0 and zeroes > 0:
				ans.append('*')
			else:
				ans.append('1'*ones)
		else:
			ans.append('0')
			i += 1

	#print(ans)
	temp = []
	last = None
	for v in ans:
		if v == '*':
			if last != '*':
				temp.append('0')
		else:
			temp.append(v)
		last = v

	return "".join(temp)

t = rri()
for _ in range(t):
	N=rri()
	S=rr()
	print(solve(N,S))
