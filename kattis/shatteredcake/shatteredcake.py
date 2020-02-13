import sys

W = int(sys.stdin.readline())
N = int(sys.stdin.readline())
area = 0
for _ in range(0, N):
    w, l = list(map(int, sys.stdin.readline().split()))
    area += w * l

L = area // W
print(str(L))
