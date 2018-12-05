import sys

def gcd(x, y):
  while(y):
    x, y = y, x % y
    
  return x

n = int(sys.stdin.readline())
line = list(map(int, sys.stdin.readline().split()))
original = line[0]

for i in range(1, len(line)):
  g = gcd(original, line[i])
  print(str(original / g)  + "/" + str(line[i] / g))
