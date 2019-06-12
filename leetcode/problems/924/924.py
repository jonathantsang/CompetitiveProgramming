class Solution:
    def minMalwareSpread(self, graph, initial):
        """
        :type graph: List[List[int]]
        :type initial: List[int]
        :rtype: int
        """
        
        colors = {} # key: node number, value: colour
        c = 0
        
        
        def dfs(node, c):
            colors[node] = c
            # Each edge from node i
            for i in range(0, len(graph[node])):
                if graph[node][i] != 0 and i not in colors:
                    dfs(i, c)
        
        for i in range(0, len(graph)):
            # For each edge from i
            if i not in colors:
                dfs(i, c)
                c += 1
                
        #print(colors)
        
        # Now find all the sections with initial
        size = collections.Counter(colors.values())
        
        #print(size)
        
        # 3. Find unique colors.
        color_count = collections.Counter()
        for node in initial:
            color_count[colors[node]] += 1
        
        #print(color_count)
        
        # 4. Answer
        ans = float('inf')
        # x in the infected nodes
        for x in initial:
            c = colors[x]
            # Check if only one from this color is infected
            if color_count[c] == 1:
                # initialize
                if ans == float('inf'):
                    ans = x
                # size of the color set is greater than  the answer's set
                #elif size[c] > size[colors[ans]]:
                    # ans = x
                # same size, smaller x value
                elif size[c] == size[colors[ans]] and x < ans:
                    ans = x

        return ans if ans < float('inf') else min(initial)    
        
        
        