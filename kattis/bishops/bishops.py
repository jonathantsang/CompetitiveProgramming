import sys

for line in sys.stdin:
    n = int(line)
    if n == 0:
        print("0")
    elif n == 1:
        print("1")
    else:
        print(str(n+n-2))
