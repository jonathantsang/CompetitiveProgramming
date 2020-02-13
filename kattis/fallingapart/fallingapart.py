import sys

n = int(sys.stdin.readline())
vals = list(map(int, sys.stdin.readline().split()))
a = 0
b = 0
turn = 0
while(len(vals) > 0):
    c = max(vals)
    vals.pop(vals.index(c))
    if turn == 0:
        a += c
    else:
        b += c
    turn = abs(turn-1)
print("{0} {1}".format(a, b))
