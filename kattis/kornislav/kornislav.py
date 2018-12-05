import sys

vals = map(int, sys.stdin.readline().split())
vals.sort()
print str(vals[0] * vals[2])