from functools import lru_cache
class Solution:
    def solve(self, weights, values, capacity, count):
        items = list(zip(weights, values))
        
        @lru_cache(None)
        def dp(i, cp, ct):
            if i == len(items) or ct == 0:
                return 0.0
            wei, val = items[i]
            ans = dp(i + 1, cp, ct)
            if cp >= wei:
                ans = max(ans, dp(i + 1, cp - wei, ct - 1) + val)
            return ans
        return int(dp(0, capacity, count))

# from awice