t = int(input())

def solve(n):
	total = 0
	# largest size first
	sizes = [2]
	amt = 2
	triangles = 1
	while amt <= n:
		# +3 each time
		# +3 for each triangle
		# +2 for last triangle
		amt += (triangles-1)*3 + 2 + 3
		triangles += 1
		sizes.append(amt)
	#print(sizes)

	idx = len(sizes)-1
	while idx >= 0:
		if sizes[idx] > n:
			idx -= 1
		else:
			n -= sizes[idx]
			total += 1
	return total

for _ in range(t):
	n = int(input())
	print(solve(n))