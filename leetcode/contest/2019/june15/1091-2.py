class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid[0][0] == 1:
            return -1
        if grid[len(grid)-1][len(grid[0])-1] == 1:
            return -1
        
        self.seen = [[float('inf') for i in range(0, len(grid[0]))] for j in range(0, len(grid))]
        self.seen[0][0] = 1
        # Check left, up, NW diag
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                for y in range(-1, 1):
                    for x in range(-1, 1):
                        # -1, -1
                        # -1, 0
                        # 0, -1
                        if y == 0 and x == 0:
                            continue
                        m = i + y
                        n = j + x
                        if m < 0 or n < 0 or m >= len(grid) or n >= len(grid[0]):
                            continue
                        if grid[m][n] == 0:
                            self.seen[i][j] = min(self.seen[i][j], self.seen[m][n]+1)
        print(self.seen)
        # Check right, down, SE diag
        for i in range(len(grid)-1, -1, -1):
            for j in range(len(grid[0])-1, -1, -1):
                for y in range(0, 1):
                    for x in range(0, 1):
                        # 0, 1
                        # 1, 0
                        # 1, 1
                        if y == 0 and x == 0:
                            continue
                        m = i + y
                        n = j + x
                        if m < 0 or n < 0 or m >= len(grid) or n >= len(grid[0]):
                            continue
                        if grid[m][n] == 0:
                            self.seen[i][j] = min(self.seen[i][j], self.seen[m][n]+1)
        print(self.seen)
        # Check NE diag, check SW diag
        for i in range(len(grid)-1, -1, -1):
            for j in range(len(grid[0])-1, -1, -1):
                # -1, 1
                # 1, -1
                for x in [-1, 1]:
                    for y in [1, -1]:
                        if x == y:
                            continue
                        m = i + y
                        n = j + x
                        if m < 0 or n < 0 or m >= len(grid) or n >= len(grid[0]):
                            continue
                        if grid[m][n] == 0:
                            self.seen[i][j] = min(self.seen[i][j], self.seen[m][n]+1)
        print(self.seen)
        return self.seen[len(grid)-1][len(grid[0])-1] if self.seen[len(grid)-1][len(grid[0])-1] != float('inf') else -1