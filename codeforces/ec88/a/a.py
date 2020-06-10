n = int(input())

rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

def solve(n,m,k):
	hand = n // k
	if hand >= m:
		return m
	else:
		return hand - ((m - hand) // (k-1) + +((m - hand) % (k-1) != 0))


for _ in range(n):
	n,m,k = rrm()
	print(solve(n,m,k))
