import sys

a, b = list(map(int, sys.stdin.readline().split()))
c, d = list(map(int, sys.stdin.readline().split()))
battery = int(sys.stdin.readline())

d = abs(a-c)+abs(b-d)
if battery < d or (battery - d) % 2 == 1:
    print("N")
else:
    print("Y") 
