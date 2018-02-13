class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        leng = len(nums)
        tail = 0
        findfirst = True
        if(leng < 2):
            return
        for i in range(0, leng):
            if(nums[i] == 0 and findfirst == True):
                tail = i
                findfirst = False
            elif(nums[i] != 0):
                temp = nums[i]
                nums[i] = 0
                nums[tail] = temp
                tail += 1