import sys

def checkValid(i, j, grid):
    # i-2, j+1
    y, x = i-2,  j+1
    if y >= 0 and x < len(grid[0]):
        if grid[y][x] == 'k':
            return False
    # i-2, j-1
    y, x = i-2, j-1
    if y >= 0 and x >= 0:
        if grid[y][x] == 'k':
            return False

    # i+2, j+1
    y, x = i+2, j+1
    if y < len(grid) and x < len(grid[0]):
        if grid[y][x] == 'k':
            return False
    # i+2, j-1
    y, x = i+2, j-1
    if y < len(grid) and x >= 0:
        if grid[y][x] == 'k':
            return False

    # i+1, j+2
    y, x = i+1, j+2
    if y < len(grid) and x < len(grid[0]):
        if grid[y][x] == 'k':
            return False
    # i-1, j+2
    y, x = i-1, j+2
    if y >= 0 and x < len(grid[0]):
        if grid[y][x] == 'k':
            return False

    # i+1, j-2
    y, x = i+1, j+2
    if y < len(grid) and x < len(grid[0]):
        if grid[y][x] == 'k':
            return False
    # i-1, j-2
    y, x = i-1, j+2
    if y >= 0 and x < len(grid[0]):
        if grid[y][x] == 'k':
            return False
    return True

grid = []
total = 0
for line in sys.stdin:
    row = []
    for c in line:
        row.append(c)
        if c == 'k':
            total += 1
    grid.append(row)

if total != 9:
    print("invalid")
    exit(0)

for i in range(0, len(grid)):
    for j in range(0, len(grid[0])):
        # grid[i][j]
        if grid[i][j] == 'k':
            if not checkValid(i, j, grid):
                print("invalid")
                exit(0)
print("valid")
