# from collections import defaultdict

rr = lambda: input()
rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

INF=float('inf')

def solve(N,S):
	if N == 1:
		return +(S != 'a')

	# divide and conquer, returns min cost to make 'c' good
	def dc(s, c, all):
		if len(s) == 1:
			return +(s != c)

		# convert all s to char c
		if all:
			amt = 0
			for char in s:
				if char != c:
					amt += 1
			return amt

		# need one half 'c'
		# need one half 'c'+1 good
		n = len(s)
		first_half = s[:n//2]
		second_half = s[n//2:]
		cost1 = dc(first_half, chr(ord(c)+1), False) + dc(second_half, c, True)
		cost2 = dc(second_half, chr(ord(c)+1), False) + dc(first_half, c, True)

		return min(cost1, cost2)

	# 'a'-good string means
	# one half 'a'
	# one half 'b'-good
	first_half = S[:N//2]
	second_half = S[N//2:]
	cost1 = dc(first_half, chr(ord('a')+1), False) + dc(second_half, 'a', True)
	cost2 = dc(second_half, chr(ord('a')+1), False) + dc(first_half, 'a', True)

	return min(cost1, cost2)

t = rri()
for _ in range(t):
	n = rri()
	s = rr()
	print(solve(n,s))
