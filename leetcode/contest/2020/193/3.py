class Solution:
    def minDays(self, A, m, k):
        if m * k > len(A): return -1
        left, right = 1, max(A)
        while left < right:
            mid = (left + right) // 2
            flow = bouq = 0
            for a in A:
                flow = 0 if a > mid else flow + 1
                if flow >= k:
                    flow = 0
                    bouq += 1
                    if bouq == m: break
            if bouq == m:
                right = mid
            else:
                left = mid + 1
        return left
