import math
import sys

leng = 1001
grid = [['.' for y in range(0, leng)] for x in range(0, leng)]

overlap = 0
for line in sys.stdin:
  arr = line.split(' ')
  id = int(arr[0][1:])
  
  push = arr[2].split(',')
  fromleft = int(push[0]) # start x
  fromtop = int(push[1][:-1]) # start y
  
  dim = arr[3].split('x')
  wide = int(dim[0])
  tall = int(dim[1])
 
  #print(fromleft, fromtop, wide, tall)
  for i in range(fromtop, fromtop+tall):
    for j in range(fromleft, fromleft+wide):
      if grid[i][j] == '.':
        grid[i][j] = 'T'
      elif grid[i][j] == 'T':
        grid[i][j] = 'X'
        overlap += 1
      elif grid[i][j] == 'X':
        pass
        
  
print(grid)
print(overlap)  
  