class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        e = defaultdict(list) # node -> list of adjacent
        for t,f in edges:
            e[t].append(f)
            e[f].append(t)

        seen = defaultdict(int) # label -> amt
        ans = [0 for _ in range(n)]
        def dfs(node, prev): # pass values seen
            seen = Counter()

            for adj in e[node]:
                if adj != prev:
                    seen += dfs(adj, node)

            # once all children done, check how many seen
            seen[labels[node]] += 1 # add own
            ans[node] = seen[labels[node]]

            return seen

        dfs(0, None)
        return ans
