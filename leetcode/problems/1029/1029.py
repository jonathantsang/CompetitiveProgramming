class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        N = len(costs) // 2
        h = []
        for i in range(len(costs)):
            a, b = costs[i]
            h.append((abs(a-b),i))
        h = sorted(h, reverse=True)
        atotal = []
        btotal = []
        for ab, i in h:
            if len(atotal) == N:
                btotal.append(costs[i][1])
            elif len(btotal) == N:
                atotal.append(costs[i][0])
            elif costs[i][0] < costs[i][1]:
                atotal.append(costs[i][0])
            else:
                btotal.append(costs[i][1])
        return sum(atotal) + sum(btotal)
