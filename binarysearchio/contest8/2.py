import heapq
class Solution:
    def solve(self, a, b, k):
        kth = 0
        if len(b) == 0:
            return len(a)
        elif k == 0:
            kth = float('inf')
        else:
            kth = heapq.nlargest(k, b)[-1]
        ans = 0
        for v in a:
            if v < kth:
                ans += 1
        return ans
