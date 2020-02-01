class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        matrix = [[0 for _ in range(0, m)] for _ in range(0, n)]
        for ind in indices:
            ri = ind[0]
            ci = ind[1]
            for i in range(0, len(matrix[0])):
                matrix[ri][i]+=1
            for i in range(0, len(matrix)):
                matrix[i][ci]+=1
        odd = 0
        for row in matrix:
            for e in row:
                if e % 2 == 1:
                    odd += 1
        return odd