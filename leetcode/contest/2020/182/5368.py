class Solution:
    def findLucky(self, arr: List[int]) -> int:
        ht = {}
        for v in arr:
            if v in ht:
                ht[v] += 1
            else:
                ht[v] = 1
        best = -1
        for v in ht:
            if v == ht[v]:
                best = max(best, v)
        return best
        