from functools import lru_cache

class Solution:
    def cherryPickup(self, A):
        R, C = len(A), len(A[0])

        @lru_cache(None)
        def dp(r, c1, c2):
            if r == R:
                return 0

            ans = 0
            for n1 in (c1 - 1, c1, c1 + 1):
                for n2 in (c2 - 1, c2, c2 + 1):
                    if 0 <= n1 < C and 0 <= n2 < C:
                        ans = max(ans, dp(r + 1, n1, n2))

            ans += A[r][c1]
            if c1 != c2:
                ans += A[r][c2]
            return ans

        return dp(0, 0, C - 1)
