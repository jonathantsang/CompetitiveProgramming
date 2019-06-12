class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix == []:
            return 0
        best = 0
        dp = [[ 0 for x in range(0, len(matrix[0])+1)] for y in range(0, len(matrix)+1)]
        for i in range(1, len(matrix)+1):
            for j in range(1, len(matrix[0])+1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
                    best = max(best, dp[i][j])
        return best * best