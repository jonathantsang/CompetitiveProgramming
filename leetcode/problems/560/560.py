class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        m = dict()
        m[0] = 1
        sum, ans = 0, 0
        for i in range(0, len(nums)):
            sum += nums[i]
            
            if (sum - k) in m:
                ans += m[sum - k]
            
            if sum in m:
                m[sum] += 1
            else:
                m[sum] = 1
        return ans