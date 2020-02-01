import sys
import math

ways = 0

def within(val, wanted):
  if val - 0.000000000001 < wanted and val + 0.000000000001 > wanted:
    return True
  else:
    return False

def dist(x1, y1, x2, y2):
  return math.sqrt(pow(y2-y1, 2) + pow(x2-x1, 2))

def rightAngle(d1, d2, d3):
  if d1 == 0 or d2 == 0 or d3 == 0:
    return False
  if within(pow(d1, 2) + pow(d2, 2), pow(d3, 2)) or \
     within(pow(d2, 2) + pow(d3, 2), pow(d1, 2)) or \
     within(pow(d3, 2) + pow(d1, 2), pow(d2, 2)):
    return True
  else:
    return False

n = sys.stdin.readline()

xVals = sys.stdin.readline()
xVals = xVals.split()
xVals = map(int, xVals)
yVals = sys.stdin.readline()
xVals = xVals.split()
yVals = map(int, yVals)

pairDist = dict()
for i in range(0, len(xVals)):
  for j in range(i+1, len(yVals)):
    distance = dist(xVals[i], yVals[i], xVals[j], yVals[j])
    if distance in pairDist:
      pairDist[distance].append([i, j])
    else:
      pairDist[distance] = [[i,j]]

## print(pairDist)

seen = dict()

for leng in pairDist:
  if len(pairDist[leng]) < 2 or leng == 0:
    continue
  else:
    ## For each pair, pick another pair to get 4 points
    for i in range(0, len(pairDist[leng])):
      for j in range(i+1, len(pairDist[leng])):
        ## Use the pair
        p1 = pairDist[leng][i][0]
        p2 = pairDist[leng][i][1]
        p3 = pairDist[leng][j][0]
        p4 = pairDist[leng][j][1]
        cannotUse = dict()
        cannotUse[p1] = 1
        cannotUse[p2] = 1
        cannotUse[p3] = 1
        cannotUse[p4] = 1
        
        ## Need 4 distinct points
        if (len(cannotUse) != 4):
          continue
        
        rectOtherSide = dist(xVals[p1], yVals[p1], xVals[p3], yVals[p3])
        rectOtherSideTwo = dist(xVals[p2], yVals[p2], xVals[p4], yVals[p4])
        
        rectOtherSideThree = dist(xVals[p1], yVals[p1], xVals[p4], yVals[p4])
        rectOtherSideFour = dist(xVals[p2], yVals[p2], xVals[p3], yVals[p3])
      
        if rectOtherSide == 0 or rectOtherSideTwo == 0 or \
           rectOtherSideThree == 0 or rectOtherSideFour == 0:
          continue
        
        ## Remove squares
        if rectOtherSide == rectOtherSideTwo and \
           rectOtherSide == rectOtherSideThree and \
           rectOtherSide == rectOtherSideFour:
          continue
        
        elif (rectOtherSide == rectOtherSideTwo and\
              rectOtherSideThree == rectOtherSideFour):
          
          a1 = rectOtherSide = dist(xVals[p1], yVals[p1], xVals[p2], yVals[p2])
          a2 = rectOtherSide = dist(xVals[p1], yVals[p1], xVals[p3], yVals[p3])
          a3 = rectOtherSide = dist(xVals[p1], yVals[p1], xVals[p4], yVals[p4])
          
          ## Remove squares
          if (a1 == a2 or a1 == a3):
            continue
          
          ## Duplicate check
          a = [p1, p2, p3, p4]
          a.sort()
          v = 0
          for c in a:
            v *= 10
            v += c
          if v in seen:
            continue
          
          seen[v] = 1
          ## Rectangle go through all points
          ## print(cannotUse)
          ## print(p1+1, p2+1, p3+1, p4+1, "is a oblong")
                    
          for m in range(0, len(xVals)):
            if m in cannotUse:
              continue
            for n in range(m+1, len(yVals)):
              if m == n or n in cannotUse:
                continue
              else:
                for k in range(n+1, len(xVals)):
                  if k == n or k == m or k in cannotUse:
                    continue
                  else:
                    print(m+1, n+1, k+1)
                    d1 = dist(xVals[m], yVals[m], xVals[n], yVals[n])
                    d2 = dist(xVals[n], yVals[n], xVals[k], yVals[k])
                    d3 = dist(xVals[m], yVals[m], xVals[k], yVals[k])
                    if d1 == 0 or d2 == 0 or d3 == 0:
                      continue
                    elif rightAngle(d1, d2, d3):
                      print(m+1, n+1, k+1, " works" )
                      print(d1, d2, d3, "dists")
                      ways+=1
print(ways)