import sys

def dist(x1, y1, x2, y2):
    return pow(x2-x1,2) + pow(y2-y1, 2)

for line in sys.stdin:
    line = list(map(float, line.split()))
    d = line[0]
    N = int(line[1])
    if d == 0.0 and N == 0:
        break
    hives = []
    for i in range(0, N):
        xy = list(map(float, sys.stdin.readline().split()))
        hives.append((xy[0], xy[1]))
    honey = {}
    for hive in hives:
        honey[hive] = 1 # 1 means sweet
    for i in range(0, len(hives)):
        for j in range(i+1, len(hives)):
            if dist(hives[i][0], hives[i][1], hives[j][0], hives[j][1]) <= pow(d, 2):
                honey[hives[i]] = 0
                honey[hives[j]] = 0
                break
    sweet = 0
    sour = 0
    for hive in honey:
        if honey[hive] == 1:
            sweet += 1
        else:
            sour += 1
    print(str(sour) + " sour, " + str(sweet) + " sweet")
