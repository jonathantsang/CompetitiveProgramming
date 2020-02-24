import sys

b, br, bs, a, aS = list(map(int, sys.stdin.readline().split()))

amt = (br - b) * bs

years = amt // aS + 1

print(str(years + a))
