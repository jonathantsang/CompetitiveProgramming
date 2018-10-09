import sys

n = int(sys.stdin.readline())
boardSize = 8
seen = [[0 for x in range(0, boardSize)] for y in range(0, boardSize)]
beginX = 0
beginY = 0

def dfs(x, y, steps):
  if x < 0 or y < 0 or x >= boardSize or y >= boardSize:
    return
  elif y == beginY and x == beginX and steps != 0:
    return  
  ## Already calc, but better
  elif seen[y][x] != 0 and seen[y][x] > steps:
    seen[y][x] = steps
    ## Possible horse moves
    ## Up
    dfs(x-1, y-2, steps+1)
    dfs(x+1, y-2, steps+1)
    ## Right
    dfs(x+2, y-1, steps+1)
    dfs(x+2, y+1, steps+1)
    ## Down
    dfs(x-1, y+2, steps+1)
    dfs(x+1, y+2, steps+1)
    ## Left
    dfs(x-2, y-1, steps+1)
    dfs(x-2, y+1, steps+1)    
  elif seen[y][x] == 0:
    seen[y][x] = steps
    ## Possible horse moves
    ## Up
    dfs(x-1, y-2, steps+1)
    dfs(x+1, y-2, steps+1)
    ## Right
    dfs(x+2, y-1, steps+1)
    dfs(x+2, y+1, steps+1)
    ## Down
    dfs(x-1, y+2, steps+1)
    dfs(x+1, y+2, steps+1)
    ## Left
    dfs(x-2, y-1, steps+1)
    dfs(x-2, y+1, steps+1)

for line in sys.stdin:

  x = ord(line[0])-ord('a') ## 'a' is 0
  y = boardSize - (int(line[1])) ## y value
  beginX = x
  beginY = y
  
  dfs(x, y, 0)
  ## print(seen)
  
  mostMoves = 0
  for y in range(0, boardSize):
    for x in range(0, boardSize):
      mostMoves = max(mostMoves, seen[y][x])
            
  hiding = []
  for y in range(0, boardSize):
      for x in range(0, boardSize):
        if mostMoves == seen[y][x]:
          hiding.append((x, y))
            
  final = str(mostMoves)
  for place in hiding:
    final += " " + chr(place[0]+97) + str(boardSize - place[1])
    
  print final
  
  ## Clear
  seen = [[0 for x in range(0, boardSize)] for y in range(0, boardSize)]
  