from functools import lru_cache

class Solution:
    def solve(self, nums, k):
        MOD = 10**9+7
        N = len(nums)

        @lru_cache(None)
        def dp(i, prev, size):
            if size == k:
                return 1
            if i == N:
                return +(size == k)

            amt = 0

            # take number
            if nums[i] > prev:
                amt += dp(i+1, nums[i], size+1)

            # don't take number
            amt += dp(i+1, prev, size)

            return amt

        ans = dp(0, -float('inf'), 0)

        return ans % MOD
