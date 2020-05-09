class Solution:
    def solve(self, nums):
        # Write your code here
        i = 0
        while i < len(nums):
            if nums[i] % 2 == 0:
                j = i + 1
                while j < len(nums):
                    if nums[j] % 2 == 0:
                        nums[i], nums[j] = nums[j], nums[i]
                        break
                    j += 1
                i = j
            i += 1
        return nums