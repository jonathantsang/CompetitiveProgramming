import math
import sys

twice = 0
three = 0
for line in sys.stdin:
  seen = dict()
  for c in line:
    if c in seen:
      seen[c] += 1
    else:
      seen[c] = 1
  
  hasTwo = False
  hasThree = False
  for key in seen:
    if seen[key] == 2:
      hasTwo = True
    if seen[key] == 3:
      hasThree = True
  if hasTwo:
    twice += 1
  if hasThree:
    three += 1
print(twice * three)