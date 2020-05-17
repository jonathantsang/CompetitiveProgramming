import sys

n = int(sys.stdin.readline())

line = list(map(int, (sys.stdin.readline().split())))
count = 0
c = 0

while(c < len(line)):
  ## disturbed
  if c+2 >= len(line):
    break
  if line[c] == 1 and line[c+1] == 0 and line[c+2] == 1:
    ## check further
    count += 1
    c = c+3
  else:
    c += 1
  

print(count)