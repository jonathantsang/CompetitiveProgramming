from collections import defaultdict

rr = lambda: input()
rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

INF=float('inf')

def solve(N,M,directed_edges,undirected_edges,ues):
	def isCycle():
		cycle = False

		def search(node,prev):
			nonlocal cycle
			nonlocal seen
			#print(node, prev, seen)

			if node in seen:
				cycle = True
				return

			seen.add(node)

			# undirected are added to directed, so only search here
			for adj in directed_edges[node]:
				search(adj, node)

			seen.remove(node) # backtracking seen

		for node in range(1,N+1):
			if cycle:
				return cycle

			seen = set()
			search(node, None)

		#print(cycle)
		return cycle

	# Make each ues directed either way and then check
	bitset = 1<<len(ues)

	# set directions
	for val in range(bitset):
		for i, (xi,yi) in enumerate(ues):

			# clear last one
			if yi in directed_edges[xi]:
				directed_edges[xi].remove(yi)
			if xi in directed_edges[yi]:
				directed_edges[yi].remove(xi)

			if val & (1<<i):
				directed_edges[xi].add(yi)
			else:
				directed_edges[yi].add(xi)

		#print("check cycle")
		#print(directed_edges)
		if not isCycle():
			print("YES")
			for xi in directed_edges:
				for yi in directed_edges[xi]:
					print(xi, yi)
			return
		#print('')

	# YES or NO
	print("NO")
	return

t = rri()
for _ in range(t):
	N,M=rrm()
	directed_edges = defaultdict(set)
	undirected_edges = defaultdict(set)
	ues = []

	for _ in range(M):
		ti,xi,yi=rrm()
		if ti == 0: # undirected
			undirected_edges[xi].add(yi)
			undirected_edges[yi].add(xi)
			ues.append((xi,yi))
		else: # directed
		 	# x->y
			directed_edges[xi].add(yi)
	solve(N,M, directed_edges, undirected_edges, ues)
