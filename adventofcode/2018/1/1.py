import math
import sys

seen = dict()
count = 0
first = 0

nums = []
for line in sys.stdin:
  if(line[0] == '-'):
    a = int(line[1:])
    nums.append(-a)
  else:
    nums.append(int(line))
  
while True:
  for n in nums:
    count += n
    
    if count in seen:
      first = count
      print("seen " + str(first) )
      exit(1)
  
    seen[count] = 1
    
print(count)
print(first)