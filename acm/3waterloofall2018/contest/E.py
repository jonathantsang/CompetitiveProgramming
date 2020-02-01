import sys

initialVals = sys.stdin.readline()
initialVals = initialVals.split()

R = int(initialVals[0])
C = int(initialVals[1])
N = int(initialVals[2])
M = int(initialVals[3])

modulo = 998244353
ways = 0

ondX = sys.stdin.readline().split()
ondY = sys.stdin.readline().split()

arr = []
for i in range(0, R):
  part = []
  for j in range(0, C):
    part.append(0)
  arr.append(part)
  
## Add Troy balls
x = 0
y = 0
for i in range(0, N):
  x = i % R
  y = i % C
  arr[x][y] += 1

## Add Onddrej balls
for i in range(0, len(ondX)):
  x = int(ondX[i])
  y = int(ondY[i])
  arr[x][y] += 1
  
print(arr)
## For each row
for i in range(0, len(arr)):
  ## Get sum, and from there decide