import sys

n = int(sys.stdin.readline())

for _ in range(0, n):
    line = sys.stdin.readline().split('\n')[0]
    L = len(line)
    sq = -1
    i = 0
    while sq < L:
        sq = pow(i, 2)
        i += 1
    M = sq
    pad = '*' * (M - L)
    line += pad
    i -= 1

    grid = [[' ' for _ in range(0, i)] for _ in range(0, i)]
    idx = 0
    for j in range(0, i):
        for k in range(0, i):
            grid[j][k] = line[idx]
            idx += 1
    ans = []
    for j in range(0, i):
        for k in range(i-1, -1, -1):
            if grid[k][j] != "*":
                ans.append(grid[k][j])
    final = "".join(ans)
    print(final)
