import collections

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        best = 0
        windowStart = 0
        minheap = []
        maxheap = []


        for i, x in enumerate(nums):
            heapq.heappush(minheap, (x, i))
            heapq.heappush(maxheap, (-x, i))

            while minheap[0][1] < windowStart:
                heapq.heappop(minheap)
            while maxheap[0][1] < windowStart:
                heapq.heappop(maxheap)

            if limit < abs(-maxheap[0][0] - minheap[0][0]):
                # pop off window
                windowStart += 1

            best = max(i - windowStart + 1, best)
            #print(minheap, maxheap, windowStart)

        return best
