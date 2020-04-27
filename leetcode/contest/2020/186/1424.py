class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        ans = []
        heap = []
        for i in range(0, len(nums)):
            for j in range(0, len(nums[i])):
                heap.append((j+i, j, nums[i][j]))
        heapq.heapify(heap)
        while len(heap) > 0:
            v = heapq.heappop(heap)
            ans.append(v[2])
        return ans
