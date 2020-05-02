import collections
import heapq

class Solution:
    def solve(self, s, k):
        # Write your code here
        v = collections.Counter(s)
        heap = []
        for i in v:
            heap.append((v[i], i))
        heapq.heapify(heap)
        ans = 0
        while len(heap) > k:
            ans += heapq.heappop(heap)[0]
        return ans
