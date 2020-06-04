from collections import defaultdict

rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

def solve(N, m, arr, topic):
    graph = defaultdict(set)
    cur = {i:1 for i in range(N)}
    for a, b in arr:
        if topic[a-1] == topic[b-1]:
            return -1
        graph[a-1].add(b-1)
        graph[b-1].add(a-1)
    final = {}
    bfs = []
    seen = set()
    for (i, n) in enumerate(topic):
        final[i] = n
        if n == 1:
            bfs.append((i))
            seen.add(i)
    ans = []

    while bfs:
        new_bfs = []
        tmp_node = set()
        for node in bfs:
            for nei in graph[node]:
                if nei in seen: continue;
                tmp_node.add(nei)
        for tmp_n in tmp_node:
            cur[tmp_n] +=1
            if cur[tmp_n] == final[tmp_n] and cur[tmp_n] == cur[node]+1:
                new_bfs.append(tmp_n)
                seen.add(tmp_n)

        ans+=bfs
        bfs = new_bfs
    if len(ans)!= N or cur!= final:
        return -1
    return ' '.join([str(i+1) for i in ans])


n, m = rrm()
graph = []
for _ in range(m):
    graph.append(rrm())
topic = rrm()
print(solve(n, m, graph, topic))
