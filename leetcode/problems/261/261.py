class Solution:
    def dfs(self, curnode, via, edges, seen):
        if curnode in seen and via not in seen[curnode]:
            return False
        if curnode in seen and via in seen[curnode]:
            return True # going backwards
        
        if curnode not in seen:
            seen[curnode] = [via]
        if curnode in seen:
            seen[curnode].append(via)
        
        if curnode in edges:
            for adj in edges[curnode]:
                if self.dfs(adj, curnode, edges, seen) == False:
                    return False
        return True
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        e = {}
        for edge in edges:
            if edge[0] in e:
                e[edge[0]].append(edge[1])
            else:
                e[edge[0]] = [edge[1]]
            if edge[1] in e:
                e[edge[1]].append(edge[0])
            else:
                e[edge[1]] = [edge[0]]
        for i in range(0, n):
            if self.dfs(i, -1, e, {}) == False:
                return False
        return True