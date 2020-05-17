import sys
import heapq

n = int(input())

edges = {} # n -> [u, v]
nodes = {} # n -> # edges
label = {} # (u, v) -> label
heap = [] # (#edges, n)

orig = []

for line in sys.stdin.readlines():
	u, v = list(map(int, line.split()))
	orig.append((u, v))
	if u in edges:
		edges[u].append(v)
	else:
		edges[u] = [v]
		nodes[u] = 1
	if v in edges:
		edges[v].append(u)
	else:
		edges[v] = [u]
		nodes[v] = 1

for n in nodes:
	heap.append((len(edges[n]), n))
heapq.heapify(heap)

counter = 0
while len(heap) > 0:
	vals = heapq.heappop(heap)
	for e in edges[vals[1]]:
		if (vals[1], e) in label or (e, vals[1]) in label:
			continue
		label[(vals[1], e)] = counter
		label[(e, vals[1])] = counter
		counter += 1
for v in orig:
	print(label[v])