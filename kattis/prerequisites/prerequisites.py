import sys

while True:
    vals = list(map(int, sys.stdin.readline().split('\n')[0].split()))
    if len(vals) == 1:
        break
    k, m = vals
    courses = set(map(int, sys.stdin.readline().split()))
    fulfill = True
    for _ in range(0, m):
        info = list(map(int, sys.stdin.readline().split()))
        n = info[0]
        need = info[1]
        c = info[2:]
        for cc in c:
            if cc in courses:
                need -= 1
        if need > 0:
            fulfill = False
    print("yes") if fulfill else print("no")
