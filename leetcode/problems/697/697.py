class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = collections.Counter()
        ht = {} # key: number, value: [first index seen, last index seen]
        for i in range(0, len(nums)):
            count[nums[i]] += 1
            if nums[i] in ht:
                ht[nums[i]][1] = i
                ht[nums[i]][2] += 1
            else:
                ht[nums[i]] = [i, i, 1]
        # find smallest subarray with degree
        d = max(count.values())
        # print(ht)
        minleng = 999999999
        for num in ht:
            if ht[num][2] == d:
                minleng = min(minleng, ht[num][1] - ht[num][0] + 1)
        return minleng