import math
import sys

def check(w, o):
  i = 0
  count = 0
  while (i < len(w)):
    if w[i] == o[i]:
      count += 1
    i += 1
  print(count)
  if count == len(w) - 1:
    return True
  return False

store = dict()
words = []
for line in sys.stdin:
  store[line] = dict()
  for c in line:
    store[line][c] = 1
  words.append(line)

for w in words:
  for o in words:
    if w == o:
      continue
    if (check(w, o)):
      print(w, o)
      exit(1)