class Solution:
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        leng = 1
        maxleng = 0
        # Key to loop is value
        ql = dict()
        for i in range(0, len(nums)):
            curnum = nums[i]
            first = i
            leng = 1
            while(curnum != first):
                if(curnum in ql):
                    leng += ql[curnum]
                    break
                curnum = nums[curnum]
                leng += 1
            if(leng > maxleng):
                ql[first] = leng
                maxleng = leng
        return maxleng