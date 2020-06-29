class Solution:
    def solve(self, nums, k):
        s = sum(nums)
        for v in nums:
            if (s - v) / (len(nums)-1) == k:
                return True
        return False
