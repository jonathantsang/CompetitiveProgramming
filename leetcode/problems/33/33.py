class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        shift = 0
        
        if nums == []:
            return -1
        
        while(left < right):
            mid = (left + right) // 2
            # 3..4..1
            if nums[mid] > nums[right]:
                left = mid+1
            # 8..2..7
            elif nums[mid] < nums[right]:
                right = mid-1
                
        shift = left if nums[left] > nums[left-1] else left-1
        #print(shift)
        
        # search on left and right
        left = 0
        right = shift
        #print(nums[left:right+1])
        while(left < right):
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid-1
            else:
                left = mid+1
        
        if nums[left] == target:
            return left
        
        left = shift+1
        right = len(nums)-1
        #print(nums[left:right+1])
        while(left < right):
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid-1
            else:
                left = mid+1
        
        if nums[left] == target:
            return left
                
        return -1