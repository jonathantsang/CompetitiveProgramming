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
            print("first " + str(first))
            leng = 1
            ql[first] = []
            while(curnum != first):
                if(curnum in ql):
                    ## Go through dictionary array
                    for ele in ql[curnum]:
                        if(ele != first):
                            leng += 1
                        else:
                            break
                    break
                ql[first].append(curnum)
                curnum = nums[curnum]
                leng += 1
            if(leng > maxleng):
                maxleng = leng
        return maxleng