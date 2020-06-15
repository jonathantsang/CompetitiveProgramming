from collections import defaultdict, deque

rr = lambda: input()
rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

INF=float('inf')

def countEdges(start, edges, subtree):
    longestPath = 0

    def longest(node, prev, edges, subtree):
        nonlocal longestPath
        if start == None:
            return 0

        paths = [0] # dummy 0 for max()
        for adj in edges[node]:
            if adj == prev or adj not in subtree:
                continue
            paths.append(longest(adj, node, edges, subtree))

        longestPath = max(longestPath, sum(paths))
        return 1 + max(paths)

    longest(start, -1, edges, subtree)
    return longestPath

def solve(N,M,pho,edges):
    start = list(pho)[0]

    subtree = set(list(pho)) # nodes in subtree
    q = deque([(start, -1, set())]) # current, prev, set of nodes
    while q:
        node, prev, vals = q.popleft()
        if node in pho:
            subtree |= vals

        for adj in edges[node]:
            if adj != prev:
                a = vals.copy()
                a.add(adj)
                q.append((adj, node, a))

    longest = countEdges(start, edges, subtree)
    return (len(subtree)-1)*2-longest

N,M=rrm()
p=rrm()
pho = {v for v in p}
edges=defaultdict(list)
for _ in range(N-1):
    t,f=rrm()
    edges[t].append(f)
    edges[f].append(t)
print(solve(N,M,pho,edges))
