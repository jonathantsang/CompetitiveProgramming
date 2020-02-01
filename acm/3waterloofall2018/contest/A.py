import sys

n = sys.stdin.readline()
line = sys.stdin.readline()
vals = line.split()

count = dict()
for v in vals:
  count[int(v)] = 1

for i in range(1, int(n)+1):
  if i not in count:
    print(i)
    break