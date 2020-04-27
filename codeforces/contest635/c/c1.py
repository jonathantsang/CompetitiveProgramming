import sys
import collections
n,k = map(int,sys.stdin.readline().split())
adj = collections.defaultdict(list)
for i in range(n-1):
	u,v = map(int,sys.stdin.readline().split())
	adj[u].append(v)
	adj[v].append(u)

visited = {}
queue = collections.deque()
parent = {}
parlist = []
nodes = []

for i in range(1,n+1):
	visited[i] = 0

visited[1] = 1
queue.append((1,-1,1))

while len(queue)!=0:
	node,par,lev = queue.popleft()
	parent[node] = (par,lev)
	parlist.append((node,lev))
	for each in adj[node]:
		if visited[each] == 0:
			visited[each] = 1
			queue.append((each,node,lev+1))

parlist.sort(key = lambda i:i[1],reverse = True)

path = {}
cal = []
ans = 0

for node,lev in parlist:
	if path.get(node) == None:
		path[node] = 1
	else:
		path[node] += 1
	if path.get(parent[node][0]) == None:
		path[parent[node][0]] = path[node]
	else:
		path[parent[node][0]] += path[node]
for i in range(1,n+1):
	cal.append(parent[i][1]-path[i])

cal.sort(reverse = True)

for i in range(k):
	ans += cal[i]

sys.stdout.write(str(ans))
