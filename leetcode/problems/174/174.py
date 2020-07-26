class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        M,N = len(dungeon), len(dungeon[0])
        dp = [[float("inf")]*(N+1) for _ in range(M+1)]
        dp[M-1][N], dp[M][N-1] = 1, 1
            
        for i in range(M-1,-1,-1):
            for j in range(N-1,-1,-1):
                dp[i][j] = max(min(dp[i+1][j],dp[i][j+1])-dungeon[i][j],1)
        
        return dp[0][0]