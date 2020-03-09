class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = [(nums[i], i) for i in range(0, len(nums))]
        arr.sort()
        
        mult = {}
        for i in range(0, len(arr)):
            if arr[i][0] not in mult:
                mult[arr[i][0]] = i
        
        ans = []
        for v in nums:
            ans.append(mult[v])
        
        return ans