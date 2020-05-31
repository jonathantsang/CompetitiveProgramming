from collections import defaultdict
import heapq

n = int(input())

# int(input())
# list(map(int, input().split()))

def solve(n, x, edges):
	# Ayush moves first
	# Ashish afterwards
	subtree = defaultdict(int) # node -> subtree size from that node (outward from special node)

	def dfs(node, d):
		if node in subtree:
			return
		subtree[node] = 1

		amt = 1 # self
		for adj in edges[node]:
			if adj not in subtree:
				amt += dfs(adj, d+1)
		subtree[node] = amt
		return amt
	dfs(x, 0)

	# want a combination of subtree sizes where it uses all but two subtrees
	# and those are at least one is even

	#print(subtree)

	vals = []
	for s in edges[x]:
		# check subtree size
		vals.append(subtree[s])
	total = sum(vals)

	#print(vals)
	if len(vals) < 2:
		return "Ayush"

	for i in range(len(vals)):
		for j in range(i+1, len(vals)):
			if vals[i] & 1 == 0 or vals[j] & 1 == 0:
				rest = total - vals[i] - vals[j]
				if rest & 1 == 0:
					return "Ayush"
	return "Ashish"


for _ in range(n):
	n, x = list(map(int, input().split()))
	edges = defaultdict(list)
	for _ in range(n-1):
		u, v = list(map(int, input().split()))
		edges[u].append(v)
		edges[v].append(u)
	print(solve(n, x, edges))
