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

def findNext():
  for c in sorted(chars):
    name = c
    # name wants to go needs deps[name]
    if name not in deps and name not in seen:
      return name
    if name in deps and name not in seen:
      possible = True
      for needed in deps[name]:
        if needed not in seen:
          possible = False
          break
      if possible:
        return name
  return -1 # None available

# First one
for c in sorted(chars):
  name = c
  if name not in deps:
    seen[name] = 1
    order += name
    break
  
print(order)
while True:
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
        break
  print(order)
  if len(chars) == len(order):
    break
  
print(order)

# workers
final = ""
w1 = 0
w2 = 0
idx = 0
seen = dict()
times = dict()

for char in order:
  times[char] = 0
  times[char] = ord(char) + 60

print(times)

totaltime = 0
idx = 0
seen = dict()
w1 = ord(findNext()) + 60
w1store = w1
w2store = 0
w2 = 0
while True:
  if w1 > 0:
    w1 -= 1
    if w1 == 0:
      seen[chr(w1store - 60 + 64)] = 1
      w1 = ord(findNext()) -64 + 60
      w1store = w1
  if w2 > 0:
    w2 -= 1
    if w2 == 0:
      seen[chr(w2store - 60 + 64)] = 1
      w2 = ord(findNext()) - 64 + 60
      w2store = w2
  totaltime += 1
  if len(seen) == len(order):
    break
  
print(totaltime) # doesn't work