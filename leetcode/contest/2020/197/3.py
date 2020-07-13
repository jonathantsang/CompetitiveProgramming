class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        e = defaultdict(list) # node -> [(prob, adj)]
        
        for i,(t,f) in enumerate(edges):
            e[t].append((succProb[i], f))
            e[f].append((succProb[i], t))
            
        # Dijkstra's BFS to end
        seen = set()
        heap = [(-1, start)] # (node, probability)
        while heap:
            nodeprob, node = heappop(heap)
            # nodeprob is negative
            nodeprob = -nodeprob
            
            if node == end:
                return nodeprob
            
            if node in seen:
                continue
            seen.add(node)
            
            for edgeprob, adj in e[node]:
                if adj in seen:
                    continue
                heappush(heap, (-edgeprob*nodeprob, adj))
        
        return 0
            