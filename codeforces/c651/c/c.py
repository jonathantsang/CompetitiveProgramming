# from collections import defaultdict
import math

rr = lambda: input()
rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

INF=float('inf')

def solve(n):
	# odd -> lost since person will divide by self to get 1
	# even -> odd divisor (if we subtract 1, lose next turn)
	orig = n

	A = "Ashishgup"
	B = "FastestFinger"

	if n == 1:
		return B
	elif n == 2:
		return A
	elif n&1:
		return A

	# even number needs at least 1 odd divisor (not 1), else Ashishgup loses
	leftover = 1 # amount left after removing odd divisor
	while not n&1:
		n //= 2 # n is largest odd factor removed
		leftover *= 2

	# check if n has more than 1 odd factor, otherwise A can alawys win
	for i in range(3,int(math.sqrt(n)+1),2):
		if n%i==0:
			return A
	if n == 1: # 1 has no other odd factor
		# no other odd factors
		return B
	elif leftover == 2:
		return B
	else:
		return A

t = rri()
for _ in range(t):
	n=rri()
	print(solve(n))
