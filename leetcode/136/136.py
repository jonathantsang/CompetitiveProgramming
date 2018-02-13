class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums) == 1):
            return nums[0]
        realsum = 0
        s = 0
        table = dict()
        for n in range(0, len(nums)):
            if nums[n] not in table:
                table[nums[n]] = True
                s += nums[n]
            realsum += nums[n]
        print(s)
        return (s * 2) - realsum
            