r, c = list(map(int, input().split()))
grid = []
for _ in range(0, r):
    row = list(input())
    grid.append(row)

seen = set() # (tuple)
x = 0
y = 0
moves = 0
while True:
    if (x, y) in seen:
        print("Lost")
        exit(0)
    seen.add((x,y))
    if grid[y][x] == 'E':
        x += 1
    elif grid[y][x] == 'W':
        x -= 1
    elif grid[y][x] == 'S':
        y += 1
    elif grid[y][x] == 'N':
        y -= 1
    elif grid[y][x] == 'T':
        print(moves)
        exit(0)
    if x < 0 or y < 0 or x >= c or y >= r:
        print("Out")
        exit(0)
    moves += 1
