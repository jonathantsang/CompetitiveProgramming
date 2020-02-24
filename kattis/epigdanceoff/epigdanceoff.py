import sys

N, M = list(map(int, sys.stdin.readline().split()))
dance = []
for _ in range(0, N):
    line = list(sys.stdin.readline())
    dance.append(line)

moves = 0
for c in range(0, M):
    blank = True
    for r in range(0, N):
        # dance[r][c]
        if dance[r][c] == "$":
            blank = False
            break
    if blank:
        moves += 1
print(moves+1)
