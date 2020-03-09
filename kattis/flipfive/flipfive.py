n = int(input())

def flip(grid, x, y):
    grid[y][x] = abs(grid[y][x] - 1)
    if x-1 >= 0:
        grid[y][x-1] = abs(grid[y][x-1] - 1)
    if x+1 <= 2:
        grid[y][x+1] = abs(grid[y][x+1] - 1)
    if y-1 >= 0:
        grid[y-1][x] = abs(grid[y-1][x] - 1)
    if y+1 <= 2:
        grid[y+1][x] = abs(grid[y+1][x] - 1)


seen = {} # seq -> moves
def minMoves(grid, moves):
    global seen
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            # flip grid[i][j]
            flip(grid, j, i)

            # Check if seen already in fewer moves
            seq = "".join("".join(list(map(str, r))) for r in grid)
            if seq in seen and seen[seq] <= moves:
                # flip back
                flip(grid, j, i)
                continue

            seen[seq] = moves+1
            minMoves(grid, moves+1)

            # flip back
            flip(grid, j, i)

for _ in range(0, n):
    seen = {}
    grid = []
    for line in range(0, 3):
        row = []
        for c in list(input().strip()):
            if c == '*':
                row.append(0)
            else:
                row.append(1)
        grid.append(row)
    # want all 1s (white)
    minMoves(grid, 0)

    print(seen["111111111"])
