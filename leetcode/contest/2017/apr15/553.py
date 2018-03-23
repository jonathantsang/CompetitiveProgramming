class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        leng = len(nums)
        if(leng == 1):
            return str(nums[0])
        if(leng == 2):
            return str(str(nums[0]) + "/" + str(nums[1]))
        newstr = str(nums[0]) + "/("
        for i in range(1, leng):
            if(i != leng - 1):
                newstr = newstr + str(nums[i]) + "/"
            else:
                newstr = newstr + str(nums[i]) + ")"
        return newstr