import collections

class Solution:
    def solve(self, source, dest, population):
        edges = collections.defaultdict(list)
        for i in range(len(source)):
            edges[source[i]].append(dest[i])
            edges[dest[i]].append(source[i])

        bestpop = 0
        selected = set() # selected
        notselected = set() # not selected
        visited = set() # seen nodes

        queue = collections.deque([(0, 1)]) # (node #, node is selected 1 or 0)
        while len(selected) + len(notselected) != len(population):
            node, sel = queue.popleft()
            for adj in edges[node]:
                if adj in visited:
                    continue
                visited.add(adj)
                if sel == 1:
                    notselected.add(adj)
                    queue.append((adj, 0))
                else:
                    selected.add(adj)
                    queue.append((adj, 1))
        # check selected
        pop = 0
        for v in selected:
            pop += population[v]
        bestpop = max(pop, bestpop)

        pop = 0
        # reverse selection
        for v in notselected:
            pop += population[v]
        bestpop = max(pop, bestpop)

        #print(selected)
        #print(notselected)

        return bestpop
