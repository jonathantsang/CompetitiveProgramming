t = int(input())

def check(arr, bitmask):
	chosen = []
	seen = set()
	for i in range(0, len(arr)):
		if bitmask & (1 << i):
			seen.add(arr[i])
			if len(seen) > 2:
				return 0 # not a three block palindrome
			chosen.append(arr[i])
	seen = set()
	changes = 0
	secondchar = None
	x = 0
	y = 0
	i = 0
	while i < len(chosen) and chosen[i] == chosen[0]:
		x += 1
		i += 1
	if i == len(chosen):
		return len(chosen)

	secondchar = chosen[i]
	while i < len(chosen) and chosen[i] == secondchar:
		y += 1
		i += 1
	if i == len(chosen):
		return 0 # not a three block palidrome

	if len(chosen) != i + x:
		return 0 # not a three block palindrome

	for j in range(i, len(chosen)):
		if chosen[j] != chosen[0]:
			return 0 # not a three block palindrome

	return len(chosen)

		


def solve(a):
	best = 0
	bitset = 1 << len(a)
	for i in range(bitset, -1, -1):
		digits = i
		if best > len(bin(digits)[2:]):
			continue
		best = max(best, check(a, digits))
	return best

for _ in range(0, t):
	n = int(input())
	arr = list(map(int, input().split()))
	soln = solve(arr)
	print(soln)