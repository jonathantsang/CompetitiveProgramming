n = int(input())

# int(input())
# list(map(int, input().split()))

def solve(a,b):
	if a == b:
		return 0
	ops = 0
	if a > b:
		while a > b and (a & 1) == 0:
			#print(a, b)
			for i in [8,4,2]:
				if (a % i) == 0:
					a //= i
					ops += 1
					break # largest first
			if a == b:
				return ops
	elif a < b:
		while a < b:
			#print(a, b)
			c = False # possible changed
			for i in [8,4,2]:
				if (a * i) <= b:
					c = True
					a *= i
					ops += 1
					break # greatest exponentiation
			if a == b:
				return ops

			if not c:
				break # no change, no way to get b from a
	return -1

for _ in range(n):
	a, b = list(map(int, input().split()))
	print(solve(a,b))
