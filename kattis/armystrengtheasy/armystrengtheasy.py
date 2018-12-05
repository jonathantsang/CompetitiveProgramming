import sys

n = int(sys.stdin.readline())
bl = sys.stdin.readline()

for i in range(0, n):
  gmg = list(map(int, sys.stdin.readline().split()))
  gNum = gmg[0]
  mgNum = gmg[1]
  
  g = list(map(int, sys.stdin.readline().split()))
  mg = list(map(int, sys.stdin.readline().split()))
  
  g.sort()
  mg.sort()
  
  gIdx = 0
  mgIdx = 0
  while gIdx < gNum and mgIdx < mgNum:
    if g[gIdx] < mg[mgIdx]:
      gIdx += 1
    elif g[gIdx] == mg[mgIdx]:
      mgIdx += 1
    else:
      mgIdx += 1

  if gIdx == gNum:
    print("MechaGodzilla")
  else:
    print("Godzilla")
  
  bl = sys.stdin.readline()