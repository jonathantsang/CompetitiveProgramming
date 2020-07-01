import sys

solved = {} # q -> [solved, time, penalty]
for line in sys.stdin:
    if line == "-1\n":
        break
    else:
        time, q, s = line.split()
        s = True if s == "right" else False
        time = int(time)
        if q not in solved:
            solved[q] = [False, 0, 0]

        if solved[q][0] == True:
            continue # skip already solved

        if s:
            solved[q][0] = True
            solved[q][1] = time
        else:
            solved[q][2] += 20
points = 0
total = 0
for q in solved:
    if solved[q][0] == True:
        points += 1
        total += solved[q][1] + solved[q][2]
print(str(points) + " " + str(total))
