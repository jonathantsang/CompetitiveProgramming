import sys

a = map(int, sys.stdin.readline().split())
b = map(int, sys.stdin.readline().split())
c = map(int, sys.stdin.readline().split())
d = [a[0], b[1]]
if d[0] == b[0]:
  d[0] = c[0]
elif d[0] == c[0]:
  d[0] = b[0]
if d[1] == c[1]:
  d[1] = a[1]
elif d[1] == a[1]:
  d[1] = c[1]
  
print str(d[0]) + " " + str(d[1])