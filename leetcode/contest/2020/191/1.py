class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m1 = max(nums[0],nums[1])
        m2 = min(nums[0],nums[1])
        for i in range(2, len(nums)):
            if nums[i] > m1:
                m2 = m1
                m1 = nums[i]
            elif nums[i] > m2:
                m2 = nums[i]
        return (m1-1)*(m2-1)
