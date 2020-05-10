import collections

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        e = collections.defaultdict(list)
        for to,fr in edges:
            e[to].append(fr)
            e[fr].append(to)

        time = 0

        def traverse(node, prev):
            total = 0
            for adj in e[node]:
                if adj == prev:
                    continue
                else:
                    costToCollect = traverse(adj, node)
                    if hasApple[adj] or costToCollect > 0:
                        total += costToCollect
                        total += 2 # go to this node AND come back
            return total

        time = traverse(0, None)

        return time
