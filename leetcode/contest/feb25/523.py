class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        total = 0
        leng = len(nums)
        for i in range(0, leng):
            total = nums[i]
            for j in range(i + 1, leng):
                total += nums[j]
                if(total == 0 and k == 0):
                    return True
                if(k != 0 and total % k == 0):
                    return True
        return False
        