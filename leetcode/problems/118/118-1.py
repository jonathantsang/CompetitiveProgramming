class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        ans = [[1]]
        for i in range(1, numRows):
            row = [1]
            for j in range(0, i-1):
                row.append(ans[-1][j] + ans[-1][j+1])
            row.append(1)
            ans.append(row)
            # print(ans)
        return ans