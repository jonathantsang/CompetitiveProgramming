class Solution:
    def traverse(self, x, y, d, grid, valid, seen):
        # print(x, y)
        # d is direction you are going
        if y < 0 or x < 0 or y >= len(grid) or x >= len(grid[0]):
            return # outside
        seen.add((x,y))
        if x == len(grid[0])-1 and y == len(grid)-1:
            self.valid = True
            return
        
        if self.valid == True:
            return
        
        if grid[y][x] == 1:
            if d == "right":
                if x+1 >= len(grid[0]):
                    return
                if grid[y][x] in valid[grid[y][x+1]][0]:
                    self.traverse(x+1, y, d, grid, valid, seen)
            elif d == "left":
                if x-1 < 0:
                    return
                if grid[y][x] in valid[grid[y][x-1]][2]:
                    self.traverse(x-1, y, d, grid, valid, seen)
        if grid[y][x] == 2:
            if d == "up":
                if y-1 < 0:
                    return
                if grid[y][x] in valid[grid[y-1][x]][3]:
                    self.traverse(x, y-1, d, grid, valid, seen)
            elif d == "down":
                if y+1 >= len(grid):
                    return
                if grid[y][x] in valid[grid[y+1][x]][1]:
                    self.traverse(x, y+1, d, grid, valid, seen)
        if grid[y][x] == 3:
            if d == "up":
                if x-1 < 0:
                    return
                if grid[y][x] in valid[grid[y][x-1]][2]:
                    self.traverse(x-1, y, "left", grid, valid, seen)
            elif d == "right":
                if y+1 >= len(grid):
                    return
                if grid[y][x] in valid[grid[y+1][x]][1]:
                    self.traverse(x, y+1, "down", grid, valid, seen)
        if grid[y][x] == 4:
            if d == "up":
                if x+1 >= len(grid[0]):
                    return
                if grid[y][x] in valid[grid[y][x+1]][0]:
                    self.traverse(x+1, y, "right", grid, valid, seen)
            elif d == "left":
                if y+1 >= len(grid):
                    return
                if grid[y][x] in valid[grid[y+1][x]][1]:
                    self.traverse(x, y+1, "down", grid, valid, seen)
        if grid[y][x] == 5:
            if d == "down":
                if x-1 < 0:
                    return
                if grid[y][x] in valid[grid[y][x-1]][2]:
                    self.traverse(x-1, y, "left", grid, valid, seen)
            elif d == "right":
                if y-1 < 0:
                    return
                if grid[y][x] in valid[grid[y-1][x]][3]:
                    self.traverse(x, y-1, "up", grid, valid, seen)
        if grid[y][x] == 6:
            if d == "down":
                if x+1 >= len(grid[0]):
                    return
                if grid[y][x] in valid[grid[y][x+1]][0]:
                    self.traverse(x+1, y, "right", grid, valid, seen)
            elif d == "left":
                if y-1 < 0:
                    return
                if grid[y][x] in valid[grid[y-1][x]][3]:
                    self.traverse(x, y-1, "up", grid, valid, seen)
            
        
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        self.valid = False
        x = 0
        y = 0
        # direction [right, down, left, up]
        
        # which piece can enter from that direction
        valid = [[{}, {}, {}, {}], 
                 [{1, 4, 6}, {}, {1, 3, 5}, {}],
                 [{}, {2, 3, 4}, {}, {2, 5, 6}],
                 [{1, 4, 6}, {}, {}, {2, 5, 6}],
                 [{}, {}, {1, 3, 5}, {2, 5, 6}],
                 [{1, 4, 6}, {2, 3, 4}, {}, {}],
                 [{}, {2, 3, 4}, {1, 3, 5}, {}]]
        
        if len(grid) == 1 and len(grid[0]) == 1:
            return True
        # print("want {0} {1}".format(len(grid)-1, len(grid[0])-1))
        
        s = {(0,0)}
        if grid[0][0] == 1 or grid[0][0] == 6: 
            self.traverse(1, 0, "right", grid, valid, s)
        elif grid[0][0] == 2 or grid[0][0] == 3:
            self.traverse(0, 1, "down", grid, valid, s)
        elif grid[0][0] == 4:
            self.traverse(1, 0, "right", grid, valid, s)
            self.traverse(0, 1, "down", grid, valid, s)
        elif grid[0][0] == 5:
            return False
        return self.valid