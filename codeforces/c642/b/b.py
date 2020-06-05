import heapq

t = int(input())

def solve(n, k, a, b):
	minheapa = a
	heapq.heapify(minheapa)

	b = list(map(lambda x: -x, b))
	maxheapb = b
	heapq.heapify(maxheapb)

	for _ in range(k):
		minval = heapq.heappop(minheapa)
		maxval = heapq.heappop(maxheapb)
		
		#print(minval, maxval)
		if minval >= -maxval:
			heapq.heappush(minheapa, minval)
			heapq.heappush(maxheapb, maxval)
			break # don't swap worse

		heapq.heappush(minheapa, -maxval)
		heapq.heappush(maxheapb, minval)

	#print(minheapa)
	total = 0
	for v in minheapa:
		total += v

	return total

for _ in range(t):
	n, k = list(map(int, input().split()))
	a = list(map(int, input().split()))
	b = list(map(int, input().split()))

	print(solve(n, k, a, b))