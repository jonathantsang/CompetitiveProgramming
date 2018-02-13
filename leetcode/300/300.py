class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSubLeng = 0
        for i in range(0, len(nums)):
            lastElement = nums[i]
            subLeng = 1
            for j in range(i + 1, len(nums)):
                if(nums[j] > lastElement):
                    subLeng += 1
                lastElement = nums[j]
            print(subLeng)
            if(subLeng > maxSubLeng):
                maxSubLeng = subLeng
        return maxSubLeng