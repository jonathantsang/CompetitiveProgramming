import sys

n = sys.stdin.readline()

for line in sys.stdin:
    time = line.split()
    dir = time[0]
    amt = int(time[1]) if time[0] == 'F' else -int(time[1])
    h = int(time[2])
    m = int(time[3])
    total = h * 60 + m + amt

    if total >= 0:
        new_h = total // 60
        new_m = total % 60
        new_h %= 24
        print(str(new_h) + " " + str(new_m))
    else:
        total += 24*60
        new_h = total // 60
        new_m = total % 60
        print(str(new_h) + " " + str(new_m))
