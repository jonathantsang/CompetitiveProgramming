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
  totaldist = 0
  for i in range(0, len(points)):
    xdiff = abs(points[i][0] - x)
    ydiff = abs(points[i][1] - y)
    totaldist += (xdiff + ydiff)
  if totaldist < 10000:
    return True
  return False

counter = 0
for i in range(0, w):
  for j in range(0, h):
    if closest(i, j):
      counter += 1
      
print("number is ", counter)
  