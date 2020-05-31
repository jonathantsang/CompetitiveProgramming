from collections import defaultdict, deque

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = defaultdict(list)
        rev = defaultdict(list)

        for t, f in connections:
            # t goes to f
            edges[t].append(f)
            rev[f].append(t)
        #print(edges, rev)

        changed = 0
        q = deque([0])
        seen = set()
        while q:
            #print(q, changed)
            v = q.popleft()
            if v in seen:
                continue
            seen.add(v)

            for adj in edges[v]:
                if adj not in seen:
                    changed += 1
                    q.append(adj)

            for adj in rev[v]:
                if adj not in seen:
                    q.append(adj)

        return changed
