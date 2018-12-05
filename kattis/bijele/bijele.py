import sys

vals = map(int, sys.stdin.readline().split())
pieces = [1,1,2,2,2,8]
ans = [0,0,0,0,0,0]
for p in range(0, len(pieces)):
  if vals[p] != pieces:
    ans[p] = pieces[p] - vals[p]

s = ""
for a in ans:
  s += " " + str(a)
  
print s[1:]