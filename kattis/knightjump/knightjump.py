import sys

n = int(sys.stdin.readline())
grid = [[100 for k in range(0, n)] for _ in range(0, n)]

def traverse(y, x, steps):
    #print(y, x)
    if y < 0 or y >= n or x < 0 or x >= n:
        return
    elif grid[y][x] <= steps:
        return
    grid[y][x] = steps
    if y == 0 and x == 0:
        return

    # directions
    traverse(y-2, x+1, steps+1)
    traverse(y-2, x-1, steps+1)

    traverse(y+2, x+1, steps+1)
    traverse(y+2, x-1, steps+1)

    traverse(y-1, x+2, steps+1)
    traverse(y+1, x+2, steps+1)

    traverse(y-1, x-2, steps+1)
    traverse(y+1, x-2, steps+1)


y = -1
x = -1
for i in range(0, n):
    line = sys.stdin.readline()
    for j in range(0, n):
        if line[j] == "K":
            x = j
            y = i
        elif line[j] == "#":
            grid[i][j] = -1

traverse(y, x, 0)

print(grid[0][0]) if grid[0][0] != 100 else print(str(-1))
