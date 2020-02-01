import sys

def checknofour(num):
    v = str(num)
    for c in v:
        if c == '4':
            return False
    return True

n = int(sys.stdin.readline())
for t in range(1, n+1):
    val = int(sys.stdin.readline())
    # 1...val-1, 2...val-2
    a = 1
    b = val-1
    while(True):
        if checknofour(a) and checknofour(b):
            break
        else:
            a += 1
            b -= 1
    print("Case #" + str(t) + ": " + str(a) + " " + str(b))
