from collections import defaultdict

class Solution:
    def solve(self, matrix, k):
        def p(d):
            for r in d:
                print(r)

        MOD = 10**9+7
        N, M = len(matrix), len(matrix[0])

        # number of possibilities for score x in hashtable
        dp = [[defaultdict(int) for _ in range(M+1)] for _ in range(N+1)]
        dp[1][1][matrix[0][0]] = 1

        for i in range(1,N+1):
            for j in range(1,M+1):
                # dp[i][j]
                if matrix[i-1][j-1] == 0:
                    # dp[i][j][k] = dp[i][j-1][k] + dp[i-1][j][k]
                    for x in range(0, k+1):
                        dp[i][j][x] += dp[i][j-1][x] + dp[i-1][j][x] % MOD

                else:
                    #dp[i][j][k] = dp[i][j-1][k-1] + dp[i-1][j][k-1]
                    for x in range(0, k+1):
                        dp[i][j][x] += dp[i][j-1][x-1] + dp[i-1][j][x-1] % MOD
        #p(dp)
        return dp[-1][-1][k] % MOD
