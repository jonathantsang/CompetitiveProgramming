import heapq

class Solution:
    def solve(self, nums, k):
        heap = []
        for n in nums:
            heap.append(-n)
        heapq.heapify(heap)

        for _ in range(k):
            top = heapq.heappop(heap)
            top += 1
            heapq.heappush(heap, top)

        return -heap[0]
