import sys

RC = list(map(float, sys.stdin.readline().split()))
R = RC[0]
C = RC[1]

PI = 3.14159265
entire = R * R * PI
cheeze = (R - C) * (R - C) * PI
print("%.6f" % (cheeze / entire * 100))