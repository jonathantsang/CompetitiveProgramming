from collections import defaultdict
import heapq

n = int(input())

# int(input())
# list(map(int, input().split()))

def solve(n, x, edges):
	# Ayush moves first
	# Ashish afterwards

	if edges[x] <= 1:
		return "Ayush"
	if n & 1 == 1:
		return "Ashish"
	else:
		return "Ayush"

for _ in range(n):
	n, x = list(map(int, input().split()))
	edges = defaultdict(int)
	for _ in range(n-1):
		u, v = list(map(int, input().split()))
		edges[u] += 1
		edges[v] += 1
	print(solve(n, x, edges))
