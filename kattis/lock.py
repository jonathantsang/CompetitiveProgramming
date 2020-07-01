import collections
import sys

n, m = list(map(int, sys.stdin.readline().split()))
# rules
rules = {}
val = 0
for i in range(0, n):
    for j in range(0, m):
        # grid[i][j]
        rules[val] = collections.Counter()
        if i != 0:
            rules[val][val-m] = 0
        if j != 0:
            rules[val][val-1]  = 0
        if i != m-1:
            rules[val][val+m] = 0
        if j != n-1:
            rules[val][val+1] = 0
        val += 1
print(rules)
