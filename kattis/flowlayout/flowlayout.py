import sys

maxL = int(sys.stdin.readline())

curX = 0
curY = 0
mostX = 0 ## global max X
mostY = 0 ## global max Y
rowX = 0 ## row X
rowY = 0 ## row Y
for rect in sys.stdin:
  dim = list(map(int, rect.split()))
  ## print("dim " + str(dim[0]) + " " + str(dim[1]))
  if dim[0] == 0:
    break
  if dim[0] == -1 and dim[1] == -1:
    print(str(mostX) + " x " + str(mostY + rowY))
    ## Reset
    curX = 0
    curY = 0
    mostX = 0
    mostY = 0
    rowX = 0
    rowY = 0
    maxL = int(sys.stdin.readline())
  else:
    ## New row
    if curX + dim[0] > maxL:
      ## Save
      mostX = max(mostX, curX)
      mostY = max(curY + rowY, mostY)
      
      ## Update
      curY += rowY
      curX = dim[0]
      
      ## Reset
      rowY = dim[1]
      rowX = dim[0]
    ## Same row
    else:
      curX += dim[0]
      mostX = max(curX, mostX)
      rowY = max(rowY, dim[1])