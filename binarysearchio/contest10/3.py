from functools import lru_cache

class Solution:
    def solve(self, nums, k):
        # subsequence take a number or not
        best = 0

        @lru_cache(None)
        def dp(i, j, odd, taken): # (prev, cur, odd#, taken#)
            nonlocal best

            #print(j, odd, taken)
            if odd >= k:
                best=max(best, taken)

            if j == len(nums):
                return

            if nums[j] > nums[i]:
                # take number
                dp(j, j+1, odd+(nums[j]&1), taken+1)

            # don't take number
            dp(i, j+1, odd, taken)

        # LIS Odd for index i to j
        for i in range(len(nums)):
            dp(i, i+1,nums[i]&1, 1)

        return best
