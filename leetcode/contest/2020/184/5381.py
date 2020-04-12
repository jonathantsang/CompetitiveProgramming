class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        ans = []
        p = collections.deque()
        for i in range(1, m+1):
            p.append(i)
        for q in queries:
            d = p.index(q)
            ans.append(d)
            p.remove(q)
            p.appendleft(q)
        return ans
