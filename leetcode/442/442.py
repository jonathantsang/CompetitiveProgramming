class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ht = dict();
        duplicates = []
        for num in nums:
            if num in ht:
                duplicates.append(num)
            else:
                ht[num] = 1
        return duplicates
        