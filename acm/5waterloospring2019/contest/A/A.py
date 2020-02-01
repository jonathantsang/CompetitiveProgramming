import sys

best = float('inf')

def findbest(order, used, tovisit, shortest):
	global best

	# print(order, tovisit)
	if len(order) == tovisit:
		total = 0
		cur = 0
		for node in order:
			total += shortest[int(cur)][int(node)]
			cur = int(node)
		# Back to beginning
		total += shortest[int(cur)][0]
		#print(order)
		#print("total: ", total)

		best = min(best, total)
	else:
		for node in shortest: # Key is visit node
			if node not in used and node != 0: # Don't go back until end
				used[node] = 1
				findbest(order+str(node), used, tovisit, shortest)
				del used[node]

def dijkstra(node, n, edges, shortest):
	dist = {}
	for i in range(0, n):
		dist[i] = float('inf')
	dist[node] = 0
	seen = {} # Set of seen nodes
	
	for times in range(0, n):
		# Not yet travelled to all
		minimum = float('inf')
		minnode = -1
		# Find next candidate closest
		for i in range(0, n):
			if (i not in seen) and dist[i] < minimum:
				minimum = dist[i]
				minnode = i

		# print(minimum, minnode)
		seen[minnode] = 1

		for v in range(0, n):
			if minnode in edges and v in edges[minnode] and \
				dist[v] > dist[minnode] + edges[minnode][v]: 
				dist[v] = min(edges[minnode][v] + dist[minnode], dist[v])

	shortest[node] = dist

case = int(sys.stdin.readline())

for i in range(1, case+1):
	best = float('inf') # Best path

	nm = list(sys.stdin.readline().split())
	edges = {} # Key: node, Value: {} Key: adjacent nodes, Value: dist
	n = int(nm[0])
	m = int(nm[1])
	for j in range(0, m):
		data = list(map(int, sys.stdin.readline().split()))
		#print(data)
		if data[0] in edges:
			edges[data[0]][data[1]] = data[2]
		else:
			edges[data[0]] = {data[1]: data[2]}
		if data[1] in edges:
			edges[data[1]][data[0]] = data[2]
		else:
			edges[data[1]] = {data[0]: data[2]}
	visit = int(sys.stdin.readline())

	# print(edges)

	shortest = {} # Key: node, Value: {} with node, shortest path distance

	dijkstra(0, n, edges, shortest)

	# Dijstrka from each node needed to visit
	for j in range(0, visit):
		node = int(sys.stdin.readline())
		dijkstra(node, n, edges, shortest)

	# Use permutations and end node back to start to calculate the best
	#print(shortest)
	findbest("", {}, visit, shortest)

	print(best)

