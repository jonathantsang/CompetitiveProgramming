class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if((len(nums) * len(nums[0])) != (r * c)):
            return nums
        col = 0
        row = 0
        count = 0
        final = []
        for rowN in range(0, r):
            final.append([])
            for num in range(0, c):
                if(col >= len(nums[row])):
                    row += 1
                    col = 0
                final[count].append(nums[row][col])
                col += 1
            count += 1
        return final