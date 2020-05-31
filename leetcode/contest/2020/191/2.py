class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        MOD = 10**9+7
        horizontalCuts.append(0)
        verticalCuts.append(0)
        horizontalCuts.append(h)
        verticalCuts.append(w)
        horizontalCuts.sort()
        verticalCuts.sort()

        # end add extra cut
        ans = 0

        hs = []
        vs = []
        for i in range(1, len(horizontalCuts)):
            hs.append(horizontalCuts[i]-horizontalCuts[i-1])
        for i in range(1, len(verticalCuts)):
            vs.append(verticalCuts[i]-verticalCuts[i-1])

        return (max(hs) * max(vs)) % MOD
