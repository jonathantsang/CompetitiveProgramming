class Solution:
    def numOfWays(self, n: int) -> int:
        modulo = 10**9 + 7
        ans = 12
        twoc = 6
        threec = 6
        for i in range(1, n):
            n_twoc = 3 * twoc + 2 * threec
            n_threec = 2 * twoc + 2 * threec
            ans = n_twoc + n_threec
            twoc = n_twoc
            threec = n_threec
        return ans % modulo
