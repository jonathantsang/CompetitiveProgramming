grid = []
for line in range(5):
    grid.append(input().split(' '))
ix, iy = -1, -1
for i in range(5):
    for j in range(5):
        if grid[i][j] == '1':
            ix = i
            iy = j
            break
print(abs(2-ix)+abs(2-iy))
