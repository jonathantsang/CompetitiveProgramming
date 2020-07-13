class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 10**9+7
        N = len(nums)

        totals = []

        for i in range(N):
            ssum = 0
            for j in range(i,N):
                ssum += nums[j]
                totals.append(ssum)

        totals.sort()
        # 1 indexed
        left -= 1
        right -= 1
        ans = sum(totals[left:right+1])

        return ans % MOD
