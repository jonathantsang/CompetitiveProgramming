import sys

n = int(sys.stdin.readline())

def second_largest(numbers):
  first, second = None, None
  total = 0
  for n in numbers:
    total += n
    if n > first:
      first, second = n, first
    elif first > n > second:
      second = n
  return total, first, second

line = list(map(int, (sys.stdin.readline().split())))
indicies = []

seen = dict()

total, maxval, second = second_largest(line)

if len(line) == 1:
  print(0)
  exit(0)
for i in range(0, len(line)):
  if line[i] in seen:
    if seen[line[i]] != -1:
      indicies.append(i+1)
      continue
    else:
      continue
    
  mv = maxval
  if line[i] == maxval:
    mv = second
  ## remove i
  removedSum = total - line[i] - mv
  if removedSum == mv:
    indicies.append(i+1)
    seen[line[i]] = 1
  else:
    seen[line[i]] = -1

print(len(indicies))
a = ""
for i in range(0, len(indicies)):
  if i != 0:
    a += " "
  a += str(indicies[i])
print(a)
  