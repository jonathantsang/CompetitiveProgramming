class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nodupe = dict();
        leng = len(nums);
        for i in range(0, leng):
            
            