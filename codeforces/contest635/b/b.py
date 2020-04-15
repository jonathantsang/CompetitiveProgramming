import math

t = int(input())

def solve(x, n, m):
	# n VA does math.floor(x/2)+10
	# m LS does x-10
	hp = x
	while hp > 0 and n > 0 and hp > 20:
		hp = math.floor(hp//2)+10
		n -= 1
	while hp > 0 and m > 0:
		hp -= 10
		m -= 1
	return hp <= 0

for _ in range(t):
	x, n, m = list(map(int, input().split()))
	print("YES") if solve(x, n, m) else print("NO")