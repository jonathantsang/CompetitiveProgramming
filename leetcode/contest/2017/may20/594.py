class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums) == 0):
            return 0
        if(len(nums) == 1):
            return 0
        maxOverall = 0
        maxSoFar = 0
        store = dict()
        ## Count how many in the array
        for elem in nums:
            if elem not in store:
                store[elem] = 1
            else:
                store[elem] += 1
        ## For each element in the array count based on store
        for i in range(0, len(nums)):
            oneMore = nums[i] + 1
            oneLess = nums[i] - 1
            maxSoFar = 0
            atLeastOne = False
            
            ## More
            if oneMore in store:
                atLeastOne = True
                maxSoFar += store[oneMore]
            if nums[i] in store and atLeastOne:
                maxSoFar += store[nums[i]]
            if(maxSoFar > maxOverall):
                maxOverall = maxSoFar
            
            ## Reset
            maxSoFar = 0
            atLeastOne = False
            ## Less    
            if oneLess in store:
                atLeastOne = True
                maxSoFar += store[oneLess]
            if nums[i] in store and atLeastOne:
                maxSoFar += store[nums[i]]
            if(maxSoFar > maxOverall):
                maxOverall = maxSoFar
        return maxOverall
            
        
        