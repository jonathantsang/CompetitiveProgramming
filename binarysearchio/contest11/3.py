from collections import defaultdict
from functools import lru_cache

class Solution:
    def solve(self, matrix):
        if not matrix:
            return 1
        MOD = 10**9+7
        ans = 0
        N,M= len(matrix), len(matrix[0])

        @lru_cache(None)
        def dp(y, usedx):
            if y == N:
                if usedx == (1 << N) - 1:
                    return 1
                return 0
            else:
                amt = 0
                for x in range(M):
                    if matrix[y][x] == 0 and usedx & 1 << x == 0:
                        amt += dp(y+1, (usedx | 1<<x))
                return amt
        ans = dp(0,0)

        return ans % MOD
