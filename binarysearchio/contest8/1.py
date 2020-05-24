class Solution:
    def solve(self, nums, k):
        tot = sum(nums)
        for i in range(len(nums)-1, -1, -1):
            if tot <= k:
                return i
            else:
                tot -= nums[i]
        return -1
