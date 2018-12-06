import math
import sys
import heapq

w = 405
h = 405

grid = [[0 for y in range(0, w)] for x in range(0, h)]

i = 0
points = []
for line in sys.stdin:
  xy = line.split(',')
  x = int(xy[0])
  y = int(xy[1])
  points.append([x, y])
  grid[y][x] = i
  i += 1
  
# x, y
def closest(x, y):
  closestdist = 999999999
  index = 0
  tied = False
  for i in range(0, len(points)):
    xdiff = abs(points[i][0] - x)
    ydiff = abs(points[i][1] - y)
    if closestdist == (xdiff + ydiff):
      tied = True
      continue
    if closestdist > (xdiff + ydiff):
      closestdist = xdiff + ydiff
      index = i
      tied = False
    
  
  if tied == True:
    return -1
  return index

for i in range(0, w):
  for j in range(0, h):
    grid[i][j] = closest(i, j)

seen = dict()
invalid = dict()
# go through
for i in range(0, w):
  for j in range(0, h):
    if grid[i][j] in seen:
      seen[grid[i][j]] += 1
    else:
      seen[grid[i][j]] = 1
      
for i in range(0, w):
  invalid[grid[0][i]] = 1
  invalid[grid[i][0]] = 1
  invalid[grid[399][i]] = 1
  invalid[grid[i][399]] = 1

H = []
for c in seen:
  H.append([seen[c], c])
  
print(grid)
print(invalid)
H.sort()
idx = len(H)-1
while(True):
  a = H[idx] 
  print(a)
  if a[1] not in invalid:
    print(a[1], "size " , a[0])
    break
  idx -= 1
  