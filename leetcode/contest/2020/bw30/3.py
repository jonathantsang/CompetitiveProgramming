class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return 0
        N=len(nums)

        nums.sort()
        ans = float('inf')

        # change 0 front, 3 back, 1 front, 2 back etc.
        # 0 -3
        # 1 -2
        # 2 -1
        for i in range(3):
            ans = min(ans, max(nums[i:-3+i]) - min(nums[i:-3+i]))

        # 3 0
        ans = min(ans, max(nums[3:]) - min(nums[3:]))

        return ans
