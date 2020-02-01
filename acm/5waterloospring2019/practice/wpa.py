import sys
import math

for line in sys.stdin:
  line = line.split()
  a = int(line[0])
  b = int(line[1])
  c = int(line[2])

  if a == 0 and b == 0 and c == 0:
    break
  
  if (math.sqrt(pow(a,2) + pow(b,2)) == c) or (math.sqrt(pow(b,2) + pow(c,2)) == a)\
     or (math.sqrt(pow(c,2) + pow(a,2)) == b):
    print("right")
  else:
    print("wrong")
  