import heapq

class Solution:
    def solve(self, nums, k):
        MOD=10**9+7
        heap = []
        maxlen = len(bin(10**9)[2:])
        for v in nums:
            b = bin(v)[2:]
            b = b[::-1]
            for i in range(maxlen):
                if i >= len(b) or b[i] == '0':
                    heap.append(2**i)

        heapq.heapify(heap)
        # print(heap)
        added = 0
        for _ in range(min(len(heap),k)):
            val = heapq.heappop(heap)
            added += val

        return (sum(nums) + added) % MOD
