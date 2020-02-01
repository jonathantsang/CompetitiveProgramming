class Solution:
    def traverse(self, grid, i, j):
        if (i, j) in self.seen:
            return self.seen[(i, j)]
        else:
            if grid[i][j] == 1:
                return True # but don't go further
            
            valid = True
            # Check if fail (edge at a border)
            if i - 1 < 0 or i + 1 >= len(grid) or j - 1 < 0 or j + 1 >= len(grid[0]):
                valid = False
                self.seen[(i, j)] = False
                return False
            self.seen[(i, j)] = valid # set for now, so doesn't go back to it
            
            # check 4 dirs up, down, left right
            a = self.traverse(grid, i-1, j)
            b = self.traverse(grid, i+1, j)
            c = self.traverse(grid, i, j-1)
            d = self.traverse(grid, i, j+1)
            if not a or not b or not c or not d:
                valid = False
            self.seen[(i, j)] = valid
            
            return valid
    
    def closedIsland(self, grid: List[List[int]]) -> int:
        self.seen = {} # Key: (i, j) -> true, false valid so far
        closed = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == 0 and (i, j) not in self.seen:
                    valid = self.traverse(grid, i, j)
                    if valid:
                        closed += 1
        return closed
                