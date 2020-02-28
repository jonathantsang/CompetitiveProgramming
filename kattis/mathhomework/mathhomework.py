import sys

zero = True
b, d, c, l = list(map(int, sys.stdin.readline().split()))
for i in range(0, l // b+1):
    for j in range(0, ((l - (b * i)) // d)+1):
        for k in range(0, ((l - (b * i)) - d * j) // c+1):
            per = i * b + j * d + c * k
            if per == l:
                zero = False
                print("{0} {1} {2}".format(i, j, k))
if zero:
    print("impossible")
