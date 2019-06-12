class Solution:
    def minMalwareSpread(self, graph, initial):
        """
        :type graph: List[List[int]]
        :type initial: List[int]
        :rtype: int
        """
        edges = {} # key: node id, value: array of adjacent nodes
        seen = {} # key: node id, value: colour of the node
        colour = 0
        
        def dfs(node, colour):
            seen[node] = colour
            if node in edges:
                for adj in edges[node]:
                    if adj not in seen:
                        dfs(adj, colour)
        
        for i in range(0, len(graph)):
            for j in range(0, len(graph[0])):
                if graph[i][j] > 0:
                    if i in edges:
                        edges[i].append(j)
                    else:
                        edges[i] = [j]
        # print(edges)
        for i in range(0, len(graph)):
            if i not in seen:
                dfs(i, colour)
                colour += 1
                
        # print(seen)
        sizesofcolors = collections.Counter(seen.values())
        # print(sizesofcolors)
        
        colour_count = collections.Counter()
        for node in initial:
            colour_count[seen[node]] += 1
        # print(colour_count)
        
        ans = min(initial)
        for node in initial:
            mycolour = seen[node] # get the colour
            # possible to remove
            if colour_count[mycolour] == 1:
                if sizesofcolors[mycolour] > sizesofcolors[seen[ans]]:
                    ans = node
                elif sizesofcolors[mycolour] == sizesofcolors[seen[ans]] and node < ans:
                    ans = node
        return ans