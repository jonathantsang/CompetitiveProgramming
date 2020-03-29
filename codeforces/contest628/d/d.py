u, v = list(map(int, input().split()))
arr = [v-1, 1]
for i in range(0, v): # length of array
	if sum(arr) == v:
		base = val[0]
		for j in range(1, len(arr)):
			base ^= arr[j]
		if base == u:
			print(len(arr), " ".join(arr))
			break
		arr[0] -= 1
		arr[1] += 1
