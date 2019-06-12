class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # for each value, perform 2 sum
        ans = []
        seen = {} # Key tuple triplet sorted, Value: 1
        # want x + y + z = 0
        for i, v in enumerate(nums):
            row = [v]
            target = -v
            ht = {}
            # 2 sum for target
            for j in range(i, len(nums)):
                w = nums[j]
                if i == j:
                    continue
                if (target - w) in ht:
                    r = [v, w, target - w]
                    r.sort()
                    a  = (r[0], r[1], r[2])
                    if a not in seen:
                        ans.append(r)
                        seen[a] = 1
                ht[w] = 1
        return ans
                    
        