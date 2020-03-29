class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        ans = []
        for i in range(0, len(matrix)):
            smallest = float('inf')
            idx = -1
            for j in range(0, len(matrix[0])):
                if matrix[i][j] < smallest:
                    smallest = matrix[i][j]
                    idx = j
            largest = -1
            for k in range(0, len(matrix)):
                largest = max(largest, matrix[k][idx])
            if largest == smallest:
                ans.append(largest)
        return ans