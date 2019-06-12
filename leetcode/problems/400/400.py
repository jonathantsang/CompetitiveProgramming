class Solution(object):
    seen = []
    def traverse(self, i, j, grid):
        if i < 0 or j < 0 or i >= len(self.seen) or j >= len(self.seen[0]):
            return
        
        if grid[i][j] == '1' and self.seen[i][j] == 0:
            self.seen[i][j] = 1
            self.traverse(i+1, j, grid)
            self.traverse(i-1, j, grid)
            self.traverse(i, j+1, grid)
            self.traverse(i, j-1, grid)
    
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid == []:
            return 0
        rows = len(grid)
        columns = len(grid[0])
        
        self.seen = [[0 for j in range(0, columns)] for i in range(0, rows)]
        
        islands = 0
        
        for i in range(0, rows):
            for j in range(0, columns):
                if self.seen[i][j] == 0 and grid[i][j] == '1':
                    islands += 1
                    self.traverse(i, j, grid)
                # print(self.seen)
        return islands
        