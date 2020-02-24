import sys

n, h, v = list(map(int, sys.stdin.readline().split()))
d = 4

largest = 0
largest = max(h * v * d, (n-h) * v * d, (n-h) * (n-v) * d, h * (n-v) * d)
print(largest)
