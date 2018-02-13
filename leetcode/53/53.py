class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_so_far = nums[0]
        max_end_here = nums[0]
        for i in range(1, len(nums)):
            max_end_here = max(nums[i], max_end_here + nums[i])
            max_so_far = max(max_so_far, max_end_here)
        return max_so_far