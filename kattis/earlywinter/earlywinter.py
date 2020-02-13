import sys

n, d = list(map(int, sys.stdin.readline().split()))
each = list(map(int, sys.stdin.readline().split()))
earliest = -1
for i, l in enumerate(each):
    if l <= d:
        earliest = i
        break
if earliest == -1:
    print("It had never snowed this early!")
else:
    print("It hadn't snowed this early in {0} years!".format(earliest))
