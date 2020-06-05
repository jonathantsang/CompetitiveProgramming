import heapq

t = int(input())

def solve(n):
	arr = [0 for _ in range(n)]

	heap = [(-n, 0, n-1)] # (how many zeroes, lo, hi)
	heapq.heapify(heap)

	i = 1
	while len(heap) > 0:
		numz, lo, hi = heapq.heappop(heap)
		numz = -numz # swap sign cause max heap
		if lo > hi:
			continue
		mid = (lo + hi) // 2
		arr[mid] = i
		i += 1

		left = 0
		right = 0
		if (hi - lo) % 2 == 0:
			# odd number of elements
			left = numz // 2
			right = numz // 2
		else:
			# even number of elements, mismatch
			left = numz // 2 - 1
			right = numz // 2

		if lo <= mid-1:
			heapq.heappush(heap, (-left, lo, mid-1))
		if mid+1 <= hi:
			heapq.heappush(heap, (-right, mid+1, hi))

	return " ".join(list(map(str, arr)))

for _ in range(t):
	n = int(input())
	print(solve(n))