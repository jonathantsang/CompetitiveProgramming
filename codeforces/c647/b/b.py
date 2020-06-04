t = int(input())

# int(input())
# list(map(int, input().split()))

def solve(n, arr):
	possible = set()
	for i in range(len(arr)):
		for j in range(i, len(arr)):
			k = arr[i] ^ arr[j]
			#print(arr[i], arr[j], arr[i] ^ arr[j])
			if k > 0:
				possible.add(k)

	arrs = set(arr)
	best = float('inf')
	#print(possible)
	for k in possible:
		created = set()
		for v in arr:
			#print(v, k, v ^ k)
			created.add(v ^ k)
		#print(created, arrs)
		if created == arrs:
			best = min(best, k)

	if best != float('inf'):
		return best
	return -1


for _ in range(t):
	n = int(input())
	arr = list(map(int, input().split()))
	print(solve(n, arr))
