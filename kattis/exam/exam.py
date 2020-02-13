import sys

k = int(sys.stdin.readline())
yours = sys.stdin.readline().split('\n')[0]
friend = sys.stdin.readline().split('\n')[0]
same = 0
diff = 0
for i in range(0, len(yours)):
    if yours[i] == friend[i]:
        same += 1
    else:
        diff += 1

maxright = len(yours) - max(0, abs(k - same))
print(maxright)
