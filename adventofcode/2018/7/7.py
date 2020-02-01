import math
import sys

deps = dict() # key is name, value is array of values needed
seen = dict() # marked seen
order = ""

chars = dict() # possible

for line in sys.stdin:
  arr = line.split(' ')
  needs = arr[1]
  step = arr[7]
  if step in deps:
    deps[step].append(needs)
  else:
    deps[step] = [needs]
    
  chars[needs] = 1
  chars[step] = 1
print(deps)

# First one
for c in sorted(chars):
  name = c
  if name not in deps:
    seen[name] = 1
    order += name
    break
  
print(order)
while True:
  # Pick alphabetically
  pos = []
  for c in sorted(chars):
    name = c
    # name wants to go needs deps[name]
    if name not in deps and name not in seen:
      order += name
      seen[name] = 1
      break
    if name in deps and name not in seen:
      possible = True
      for needed in deps[name]:
        if needed not in seen:
          possible = False
          break
      if possible:
        order += name
        seen[name] = 1          
        pos.append(name)
        break
  print(order)
  if len(chars) == len(order):
    break
  
print(order)