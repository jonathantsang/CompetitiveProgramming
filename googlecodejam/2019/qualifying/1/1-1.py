import sys

n = int(sys.stdin.readline())
for t in range(1, n+1):
    val = sys.stdin.readline().split('\n')[0]
    # 1...val-1, 2...val-2
    a = ""
    b = ""
    for i in range(len(val)-1, -1, -1):
        digit = int(val[i])
        if digit == 4:
            a = "2" + a
            b = "2" + b
        else:
            a = str(digit) + a
            b = "0" + b
    print("Case #" + str(t) + ": " + str(int(a)) + " " + str(int(b)))

