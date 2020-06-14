class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sums = []
        sumsofar = 0
        for v in nums:
            sumsofar +=v
            sums.append(sumsofar)
        return sums
