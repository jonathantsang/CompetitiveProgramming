import sys
import math

def dist(x1, y1, x2, y2):
    return math.sqrt(pow(x1-x2, 2)+pow(y1-y2, 2))

pos = {}
for i in range(0, 3):
    nums = list(map(int, sys.stdin.readline().split()))
    for j in range(0, 3):
        pos[nums[j]] = (i, j)

# find i from x, y
d = 0
cur = pos[1]
for i in range(2, 10):
    next = pos[i]
    d += dist(cur[0], cur[1], next[0], next[1])
    cur = pos[i]

print(d)
