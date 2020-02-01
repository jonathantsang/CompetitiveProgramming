class Solution(object):
    def search(self, i, j, dist, grid):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            return
        if grid[i][j] == 1:
            return
        if self.seen[i][j] < dist:
            return
        self.seen[i][j] = min(self.seen[i][j], dist)
        for y in range(-1, 2):
            for x in range(-1, 2):
                if y == 0 and x == 0:
                    continue
                m = i + y
                n = j + x
                if m < 0 or n < 0 or m >= len(grid) or n >= len(grid[0]):
                    continue
                if grid[m][n] == 0:
                    self.search(m, n, dist+1, grid)
                
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.shortest = float('inf')
        self.seen = [[float('inf') for i in range(0, len(grid[0]))] for j in range(0, len(grid))]
        
        if grid[0][0] == 1:
            return -1
        if grid[len(grid)-1][len(grid[0])-1] == 1:
            return -1
        self.search(0, 0, 0, grid)
        return self.seen[len(grid)-1][len(grid[0])-1]+1 if self.seen[len(grid)-1][len(grid[0])-1] != float('inf') else -1