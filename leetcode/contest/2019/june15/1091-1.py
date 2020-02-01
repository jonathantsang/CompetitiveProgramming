class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.seen = [[float('inf') for i in range(0, len(grid[0]))] for j in range(0, len(grid))]
        
        if grid[0][0] == 1:
            return -1
        if grid[len(grid)-1][len(grid[0])-1] == 1:
            return -1
        
        # (i, j, dist)
        self.seen[0][0] = 1
        queue = collections.deque([(0,0)])
        while len(queue) > 0:
            p = queue.popleft()
            i = p[0]
            j = p[1]
            if i == j == len(grid)-1:
                return self.seen[i][j]
            
            for y in (-1, 0, 1):
                for x in (-1, 0, 1):
                    if y == 0 and x == 0:
                        continue
                    m = i + y
                    n = j + x
                    if m < 0 or n < 0 or m >= len(grid) or n >= len(grid[0]):
                        continue
                        
                    if grid[m][n] == 0 and (self.seen[i][j] + 1) < self.seen[m][n]:
                        self.seen[m][n] = self.seen[i][j] + 1
                        queue.append((m, n))
        return -1