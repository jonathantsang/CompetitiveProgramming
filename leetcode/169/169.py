import math

## Uses Python 2.7 on Leetcode
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ht = dict()
        leng = len(nums)
        majority = math.ceil(leng / 2)
        for num in nums:
            if num in ht:
                ht[num] += 1
                if ht[num] >= majority:
                    return num
            else:
                ht[num] = 1