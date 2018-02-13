class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        arr = []
        added = 0
        total = 0
        ## Construct the first arr
        for num in nums:
            added += num
            if(added == k):
                total += 1
            arr.append(added)
        ## Linear pass 
        for j in range(0, len(arr)):
            for i in range(j + 1, len(arr)):
                arr[i] -= nums[j]
                if(arr[i] == k):
                    total += 1
        return total