import sys

n = int(sys.stdin.readline())

for i in range(0, n):
  line = sys.stdin.readline()
  abk = list(map(int, line.split()))
  a = abk[0]
  b = abk[1]
  k = abk[2]
  
  x = 0
  ## k times
  x += a * ((k + 1) / 2)
  x -= b * (k / 2)
  print(x)
  