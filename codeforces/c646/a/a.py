n = int(input())

# int(input())
# list(map(int, input().split()))

def solve(n, x, arr):
	odd = 0
	even = 0
	for v in arr:
		if v & 1 == 1:
			odd += 1
		else:
			even += 1
	if odd == 0:
		return "No"
	else:
		x -= 1 # use at least one odd
		odd -= 1

		if x >= odd:
			# use most odd pairs possible
			if odd & 1 == 0:
				x -= odd
			else:
				x -= (odd-1)
		elif x < odd:
			# use most odd pairs possible
			if x & 1 == 0:
				x -= odd
			else:
				x -= (x-1)

		if x <= 0:
			return "Yes"

		if x <= even:
			return "Yes"

		return "No"

for _ in range(n):
	n, x = list(map(int, input().split()))
	arr = list(map(int, input().split()))
	print(solve(n, x, arr))
