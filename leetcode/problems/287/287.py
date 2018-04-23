class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ind = 0
        while(True):
            if(nums[ind] < 0):
                return ind
            else:
                nums[ind] = -nums[ind]
                ind = -nums[ind]