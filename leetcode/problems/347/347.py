class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ht = {} # number -> count
        for n in nums:
            if n in ht:
                ht[n] += 1
            else:
                ht[n] = 1
        heap = []
        for num in ht:
            heap.append((-ht[num], num))
        heapq.heapify(heap)
        ans = []
        for i in range(0, k):
            ans.append(heapq.heappop(heap)[1])
        return ans