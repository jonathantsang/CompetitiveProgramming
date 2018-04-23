class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        leng = len(nums)
        if(leng == 0):
            return 0
        
        include = 0
        exclude = 0
        new = 0
        for i in nums:
            if(exclude > include):
                new = exclude
            else:
                new = include
            print("n:" + str(new) + "\n")
            include = exclude + i
            print("i:" + str(include) + "\n")
            exclude = new
            print("e:" + str(exclude) +"\n")
        return max(exclude, include)