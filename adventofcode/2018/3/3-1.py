import math
import sys

leng = 1001
grid = [['.' for y in range(0, leng)] for x in range(0, leng)]

cuts = []

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
 
  #print(id, fromleft, fromtop, wide, tall)
  cuts.append([id, fromleft, fromtop, wide, tall])
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

nooverlap = 0
for cut in cuts:
  fail = False  
  id = cut[0]
  fromleft = int(cut[1])
  fromtop = int(cut[2])
  wide = int(cut[3])
  tall = int(cut[4])
  
  for i in range(fromtop, fromtop+tall):
    for j in range(fromleft, fromleft+wide):
      if grid[i][j] == 'T':
        pass
      elif grid[i][j] == 'X':
        # false
        fail = True
        break
    if fail:
      break
  if not fail:
    print(id, " not fail")
    break
  
  

  