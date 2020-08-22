# from collections import defaultdict

#import io, os, math
#input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

rr = lambda: input()
rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

INF=float('inf')

def solve(N,S):
	ans = [] # subsequence it belongs to

	zero = [] # subseq # end on zero
	one = [] # subseq # end on one

	i = 1
	for c in S:
		if c == '0':
			if one:
				o = one.pop()
				zero.append(o)
				ans.append(str(o))
			else:
				zero.append(i)
				ans.append(str(i))
				i+=1
		elif c == '1':
			if zero:
				z = zero.pop()
				one.append(z)
				ans.append(str(z))
			else:
				one.append(i)
				ans.append(str(i))
				i+=1

	subseq = len(zero) + len(one)
	print(subseq)
	print(' '.join(ans))

t = rri()
for _ in range(t):
	N=rri()
	S=rr()
	solve(N,S)
