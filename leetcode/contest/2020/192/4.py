class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:

        @lru_cache(None)
        def dp(idx, prevcolor, groups):
            #print(idx, prevcolor, costsofar, groups)
            ans = float('inf')

            if idx == len(houses):
                return 0 if groups == target else float('inf')

            # Leave it as is if it is not 0
            if houses[idx] != 0:
                housecolor = houses[idx]-1 # colors are 1 indexed: houses[idx]-1
                bns = float('inf')

                # same color as previous
                if housecolor == prevcolor:
                    bns = dp(idx+1, prevcolor, groups)
                # different color from previous
                else:
                    bns = dp(idx+1, housecolor, groups+1)

                return bns
            else:
                bns = float('inf')
                # Attempt to paint
                if groups == target: # must paint same type if out of groups
                    ans = cost[idx][prevcolor] + dp(idx+1, prevcolor, groups)
                else:
                    for i, colorcost in enumerate(cost[idx]):
                        if i == prevcolor:
                            bns = colorcost + dp(idx+1, i, groups)
                        else:
                            bns = colorcost + dp(idx+1, i, groups+1)

                        ans = min(ans, bns)
                return ans

        ans = dp(0, -1, 0)

        if ans == float('inf'):
            return -1
        else:
            return ans
