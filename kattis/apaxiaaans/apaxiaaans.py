import sys

name = sys.stdin.readline()
final = ""
last = ""
for c in name:
  if c != last:
    final += c
  last = c

print(final)