import sys
import math

def prime(n):
    if n & 1 == 0:
        return False
    d= 3
    while d * d <= n:
        if n % d == 0:
            return False
        d= d + 2
    return True

n = int(sys.stdin.readline())
for i in range(0, n):
    lengs = sys.stdin.readline().split()
    a = int(lengs[0])
    b = int(lengs[1])
    a1 = (a - b)
    a2 = (a + b)
    area = (a - b) * (a + b)
    if (prime(a1) == True and a2 == 1) or (prime(a2) == True and a1 == 1):
        print "YES"
    else:
        print "NO"