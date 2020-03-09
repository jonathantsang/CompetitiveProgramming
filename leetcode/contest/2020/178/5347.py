class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        costs = [[float('inf') for _ in range(0, len(grid[0]))] for i in range(0, len(grid))]
        costs[0][0] = 0
        
        diff = True
        
        while diff:
            old = sum(sum(v) for v in costs)
            # left and down
            for i in range(0, len(grid)):
                for j in range(0, len(grid[0])):
                    # grid[i][j]

                    # check left
                    if j > 0 and grid[i][j-1] == 1:
                        # free since =>
                        costs[i][j] = min(costs[i][j], costs[i][j-1])

                    # check down
                    if i > 0 and grid[i-1][j] == 3:
                        # free since down arrow
                        costs[i][j] = min(costs[i][j], costs[i-1][j])

                    if i > 0:
                        costs[i][j] = min(costs[i][j], costs[i-1][j]+1)
                    if j > 0:
                        costs[i][j] = min(costs[i][j], costs[i][j-1]+1)
            # right and up
            for i in range(len(grid)-1, -1, -1):
                for j in range(len(grid[0])-1, -1, -1):
                    # grid[i][j]

                    # check right
                    if j < len(grid[0])-1 and grid[i][j+1] == 2:
                        # free since <=
                        costs[i][j] = min(costs[i][j], costs[i][j+1])

                    # check up
                    if i < len(grid)-1 and grid[i+1][j] == 4:
                        # free since up arrow
                        costs[i][j] = min(costs[i][j], costs[i+1][j])

                    if i < len(grid)-1:
                        costs[i][j] = min(costs[i][j], costs[i+1][j]+1)
                    if j < len(grid[0])-1:
                        costs[i][j] = min(costs[i][j], costs[i][j+1]+1)
            new = sum(sum(v) for v in costs)
            if old == new:
                diff = False
                break
        return costs[-1][-1]