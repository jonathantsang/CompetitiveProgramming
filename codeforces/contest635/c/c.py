import collections
import heapq

n, k = list(map(int, input().split()))

# def totalNumChildren(node, usedOnPath, subtreeSize):
# 	total = 0
# 	if node not in usedOnPath:
# 		subtreeSize[node] = 0
# 		return 0

# 	for adj in usedOnPath[node]:
# 		if adj in subtreeSize:
# 			total += subtreeSize[adj]
# 		else:
# 			adj_total = totalNumChildren(adj, usedOnPath, subtreeSize)
# 			subtreeSize[adj] = adj_total
# 			total += adj_total + 1
# 	subtreeSize[node] = total
# 	return total

def dfs(node, d, edges, depth, subtreeSize):
	if node in depth and depth[node] < d:
		return 0
	depth[node] = d

	total = 0
	for adj in edges[node]:
		if adj not in depth:
 			childTree = dfs(adj, d+1, edges, depth, subtreeSize)
 			subtreeSize[adj] = childTree
 			total += childTree + 1

	subtreeSize[node] = total
	return total

def solve(edges, depth):
	subtreeSize = collections.defaultdict(int) # node -> # nodes in subtree

	dfs(1, 0, edges, depth, subtreeSize)

	nodes = []
	for node in depth:
		if node not in subtreeSize:
			subtreeSize[node] = 0
		nodes.append(-depth[node] + subtreeSize[node]) # depth
	heapq.heapify(nodes)

	ans = 0
	for _ in range(k):
		top = heapq.heappop(nodes)
		ans += -top
	return ans

edges = collections.defaultdict(list) #node -> [adj nodes]
depth = collections.defaultdict(int) #node -> depth
for _ in range(n-1):
	u, v = list(map(int, input().split()))
	edges[u].append(v)
	edges[v].append(u)
print(solve(edges, depth))