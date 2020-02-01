import sys

leng = int(sys.stdin.readline())
s = sys.stdin.readline()

def transformCost(before, after):
  a = ord(after)-65
  b = ord(before)-65
  # print(before, after, b, a)
  smaller = min(a, b)
  bigger = max(a, b)
  return min(abs(b - a), abs(26  - bigger + smaller))

genome = 'ACTG'
mincost = float('inf')
# Each 4 segment in the string
for i in range(0, leng-3):
  cost = 0
  # Get cost of genome transform
  for j in range(0, len(genome)):
    cost += transformCost(s[i+j], genome[j])
  mincost = min(mincost, cost)
print(mincost)