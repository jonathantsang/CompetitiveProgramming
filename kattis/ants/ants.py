import sys

n = int(sys.stdin.readline())

for _ in range(0, n):
    l, a = list(map(int, sys.stdin.readline().split()))
    longest = -float('inf')
    shortest = -float('inf')
    counted = 0
    while(counted != a):
        ants = list(map(int, sys.stdin.readline().split()))
        counted += len(ants)
        for num in ants:
            longest = max(longest, l - num, num)
            shortest = max(shortest, min(l - num, num))
    print("{0} {1}".format(shortest, longest))
