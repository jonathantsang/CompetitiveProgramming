class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        leng = len(nums)
        nums.sort()
        ht = dict()
        j = 1
        i = 0
        while(j < leng):
            if(i == j):
                j += 1  
            elif(abs(nums[j] - nums[i]) == k and nums[i] not in ht):
                count += 1
                ht[nums[i]] = nums[j]
                i += 1
                j += 1
            elif(abs(nums[j] - nums[i]) < k):
                j += 1
            elif(abs(nums[j] - nums[i]) > k):
                i += 1
            else:
                i += 1
                j += 1
        return count
                    