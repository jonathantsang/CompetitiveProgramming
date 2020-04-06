class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        ns = sorted(nums, reverse=True)
        larger = 0
        lv = []
        for v in ns:
            if larger > total:
                break
            total -= v
            larger += v
            lv.append(v)
        return lv