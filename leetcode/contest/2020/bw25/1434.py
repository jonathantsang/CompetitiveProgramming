from functools import lru_cache

class Solution(object):
    def numberWays(self, hats):
        MOD = 10 ** 9 + 7
        A = list(map(set, hats))
        N = len(A)

        """
        mask = []
        for r, row in enumerate(hats):
            mask = 0
            for i, c in enumerate(row):
                row[i] -= 1
                mask |= 1 << row[i]
            masks.append(mask)
        """
        target = 1 << N
        target -= 1

        @lru_cache(None)
        def dp(mask, hat_num):
            if mask == target:
                return 1
            ans = 0
            for bit in range(N):
                if (mask >> bit) & 1 == 0:
                    # try to wear hat num
                    for h in A[bit]:
                        if h > hat_num:
                            ans += dp(mask ^ (1 << bit), h)
                            ans %= MOD
            return ans

        return dp(0, 0) % MOD
