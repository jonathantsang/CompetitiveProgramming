import collections

t = int(input())

def solve(n, arr):
	arr = collections.deque(arr)
	a = 0
	b = 0
	turns = 0
	turn = 0
	last = 0
	while len(arr) > 0:
		#print(arr)
		turns += 1
		ate = 0
		while ate <= last and len(arr) > 0:
			if turn == 0:
				ate += arr.popleft()
			else:
				ate += arr.pop()
		last = ate
		if turn == 0:
			a += ate
		else:
			b += ate
		turn ^= 1
	print(turns, a, b)



for _ in range(t):
	n = int(input())
	arr = list(map(int, input().split()))
	solve(n, arr)