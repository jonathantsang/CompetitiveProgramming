class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        record=[nums[0],nums[0]]
        res=nums[0]
        
        for v in nums[1:]:
            record=[max(v,v*record[0],v*record[1]),min(v,v*record[0],v*record[1])]
            res=max(res,record[0])
            
        return res