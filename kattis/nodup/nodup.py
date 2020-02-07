import sys

line = sys.stdin.readline().split()

d = {}
fail = False
for word in line:
    if word in d:
        fail = True
        break
    else:
        d[word] = 1
print("yes") if not fail else print("no")
