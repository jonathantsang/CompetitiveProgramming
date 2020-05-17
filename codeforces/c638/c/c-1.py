import heapq

t = int(input())

def solve(n, k, s):
	heap = []
	for c in s:
		# ord
		heap.append((ord(c), c))
	heapq.heapify(heap)
	print(heap)
	ans = []
	while len(heap) > 0:
		# Pop off k
		same = -1 # replaced with (ord(c), c)
		allSame = True
		for _ in range(k):
			if len(heap) == 0:
				# keep last one
				break

			v = heapq.heappop(heap)

			if same == -1:
				same = v
			else:
				if same != v:
					allSame = False
					same = v # keep largest value

		ans.append(same[1])
		if not allSame:
			break

	return "".join(ans)


for _ in range(t):
	n, k = list(map(int, input().split()))
	s = input()
	print(solve(n, k, s))