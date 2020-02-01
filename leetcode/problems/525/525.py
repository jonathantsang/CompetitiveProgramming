class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dp = [0 for i in range(0, len(nums))] # Each index has a count with -1 for 0, 1 for 1, and 2, 3, etc. for current sum
        if nums == []:
            return 0
        if nums[0] == 0:
            dp[0] = -1
        else:
            dp[0] = 1
        for i in range(1, len(nums)):
            if nums[i] == 0:
                dp[i] = dp[i - 1] -1
            else:
                dp[i] = dp[i - 1] +1
        # print(dp)
        # Last seen certain numbers
        ht = { 0: -1 } # Key: value, Value: index last seen
        bestlen = 0
        for i in range(0, len(nums)):
            if dp[i] not in ht:
                ht[dp[i]] = i
            else:
                bestlen = max(bestlen, i - ht[dp[i]])
                # ht[dp[i]] = i
        return bestlen
                