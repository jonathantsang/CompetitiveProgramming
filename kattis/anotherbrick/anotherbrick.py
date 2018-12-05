import sys

hwn = list(map(int, sys.stdin.readline().split()))
h = hwn[0]
w = hwn[1]
n = hwn[2]

bricks = list(map(int, sys.stdin.readline().split()))

overallLevel = 0
layer = 0

for brick in bricks:
  layer += brick
  if layer == w:
    overallLevel += 1
    layer = 0
    if overallLevel == h:
        print ("YES")
        break
  elif layer > w:
    print ("NO")
    break