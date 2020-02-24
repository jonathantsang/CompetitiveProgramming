import sys

a, b, c = list(map(int, sys.stdin.readline().split()))
i, j, k = list(map(int, sys.stdin.readline().split()))


lr = min(a / i, b / j, c / k)
print("{0} {1} {2}".format( a - i * lr, b - j * lr, c - k * lr))
