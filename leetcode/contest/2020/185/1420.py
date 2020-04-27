class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7
        self.ans = 0

        @lru_cache(None)
        def dfs(n0, m0, k0):
            if k < 1:
                return 0
            if n0 == 0:
                if k0 == 0:
                    return 1
                return 0

            total = 0
            # split
            for a in range(1, m + 1):
                if a > m0: #newmax
                    total += dfs(n0-1, a, k0-1)
                    total %= MOD
                else:
                    total += dfs(n0-1, m0, k0)
                    total %= MOD

            return total

        self.ans += dfs(n, -1, k)

        return self.ans % MOD
