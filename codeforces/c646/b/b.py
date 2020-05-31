from itertools import groupby
import collections

n = int(input())

# int(input())
# list(map(int, input().split()))

def solve(s):
	# 1001 has subsequence -> 101
	blocks = collections.deque([''.join(g) for _, g in groupby(s)])
	#print(blocks)
	ops = float('inf')

	ones = [0] # at each index how many 1s on left
	zeroes = [0] # at each index how many 0s on left
	for b in blocks:
		# either partition 1s | 0s
		# or 0s | 1s
		if b[0] == '1':
			ones.append(ones[-1]+len(b))
			zeroes.append(zeroes[-1])
		else:
			ones.append(ones[-1])
			zeroes.append(zeroes[-1]+len(b))

	#print(ones, zeroes)
	total1 = ones[-1]
	total0 = zeroes[-1]
	for o,z in zip(ones, zeroes):
		# cost to leave left as 1 and right as 0
		cost = z + total1 - o
		ops = min(cost, ops)

		# cost to leave left as 0 and right as 1
		cost = o + total0 - z
		ops = min(cost, ops)

	return ops

for _ in range(n):
	s = input()
	print(solve(s))
