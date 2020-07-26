from collections import defaultdict

class Solution:
    def solve(self, matrix):
        N,M = len(matrix), len(matrix[0])

        best = 0

        # get total number of 1s in the matrix
        total = 0
        for r in matrix:
            total += sum(r)

        rowsum = defaultdict(int) # row sum at row i
        colsum = defaultdict(int) # col sum at column i

        for i,row in enumerate(matrix):
            rowsum[i] = sum(row)
        for i,col in enumerate(zip(*matrix)):
            colsum[i] = sum(col)

        ans = 0
        for i in range(N):
            for j in range(M):
                # matrix[i][j] being 1 has it counted twice so -2 if it is 1
                ones = rowsum[i] + colsum[j] - 2 * matrix[i][j]

                # from the row (N) and column (M) subtract ones to get zeroes
                zeroes = N + M - 2 - ones

                # Get the new number of 1s and zeroes using the total, ones, and zeroes
                cand = total - ones + zeroes

                ans = max(ans, cand)

        return ans
