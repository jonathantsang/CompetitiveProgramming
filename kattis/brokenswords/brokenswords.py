import sys

n = int(sys.stdin.readline())
TB = 0
LR = 0
for _ in range(0, n):
    T, B, L, R = list(map(int, list(sys.stdin.readline().split('\n')[0])))
    TB += abs(T-1) + abs(B-1)
    LR += abs(L-1) + abs(R-1)
swords = min(TB // 2, LR // 2)
v_left = TB - swords * 2
h_left = LR - swords * 2
print("{0} {1} {2}".format(swords, v_left, h_left))
