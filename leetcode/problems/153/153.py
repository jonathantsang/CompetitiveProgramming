class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while(left < right):
            mid = (left + right) // 2
            
            # 4...7...2, go right
            if nums[mid] > nums[right]:
                left = mid+1
            # 9..4...8
            elif nums[mid] < nums[right]:
                right = mid
        return nums[left]