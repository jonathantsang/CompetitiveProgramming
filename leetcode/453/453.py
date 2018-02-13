class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        leng = len(nums)
        if(leng == 1):
            return 0
        maxv = max(nums[0], nums[1])
        minv = min(nums[0], nums[1])
        sums = 0
        ## Find the max in the array
        for val in nums:
            sums = sums + val
            if(val > maxv):
                maxv = val
            if(val < minv):
                minv = val
        bound = maxv * leng
        difference = bound - sums
        incrementtotal = leng - 1
        cool = difference // incrementtotal + difference % incrementtotal
        if(difference % incrementtotal > 0):
            cool = cool + 1
        ## To account for off by one
        cooler = cool
        if(maxv - minv > incrementtotal):
            cooler = cool + leng
        return cooler
        
            
        