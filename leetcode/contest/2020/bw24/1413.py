class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        d = 0
        mval = float('inf')
        for n in nums:
            d += n
            mval = min(d, mval)
        return max(-mval+1, 1)