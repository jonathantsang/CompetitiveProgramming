class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        newl = nums[:]
        newl.sort()
        start = 0
        end = 0
        for i in range(0, len(nums)):
            if(newl[i] != nums[i]):
                start = i
                break
        for j in range(len(nums) - 1, -1, -1):
            if(newl[j] != nums[j]):
                end = j
                break
        if(start == 0 and end == 0):
            return 0
        return end+1 - start