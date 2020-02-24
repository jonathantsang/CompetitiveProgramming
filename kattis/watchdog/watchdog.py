import sys

def inrange(i, j, leash, hatch):
    return (pow(i-hatch[0], 2) + pow(j - h[1], 2)) <= pow(leash, 2)

n = int(sys.stdin.readline())
for _ in range(0, n):
    s, h = list(map(int, sys.stdin.readline().split()))
    hatches = []
    for _ in range(0, h):
        x, y = list(map(int, sys.stdin.readline().split()))
        hatches.append((x, y))

    found = False
    # smallest x, smallest y
    for i in range(s-1, -1, -1):
        for j in range(s-1, -1, -1):
            leash = min(i, s-i, j, s-j)

            works = True
            for h in hatches:
                # can't be attached at hatch
                if h[0] == i and h[1] == j:
                    works = False
                # see if it is in range
                if not inrange(i, j, leash, h):
                    works = False

            if works:
                found = True
                xloc = i
                yloc = j

    if found:
        print("{0} {1}".format(xloc, yloc))
    else:
        print("poodle")
