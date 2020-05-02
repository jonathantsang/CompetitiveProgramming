class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        best = max(candies)
        ans = []
        for k in candies:
            if k + extraCandies >= best:
                ans.append(True)
            else:
                ans.append(False)
        return ans
