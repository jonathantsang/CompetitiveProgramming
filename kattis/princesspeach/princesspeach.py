import sys

N, Y = list(map(int, sys.stdin.readline().split()))

seen = {}
for line in sys.stdin:
    seen[int(line)] = 1

for i in range(0, N):
    if i not in seen:
        print(i)
print("Mario got " + str(len(seen)) + " of the dangerous obstacles.")
