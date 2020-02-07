import sys
import math

def contained(x1, y1, x2, y2, v):
    r = v / math.pi # r squared

    dist = pow(x1-x2, 2) + pow(y1-y2,2) # dist squared

    if dist > r:
        return False
    else:
        return True

n = int(sys.stdin.readline())

for j in range(0, n):
    d = int(sys.stdin.readline())
    drops = []
    for i in range(0, d):
        vals = sys.stdin.readline().split()
        x, y, v = float(vals[0]), float(vals[1]), float(vals[2])
        color = vals[3]
        drops.append((x, y, v, color))
    q = int(sys.stdin.readline())
    for i in range(0, q):
        x, y = list(map(float, sys.stdin.readline().split()))
        color = "white"
        for drop in drops:
            if contained(x, y, drop[0], drop[1], drop[2]):
                color = drop[3]
        print(color)
