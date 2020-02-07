import sys

day = 1
first = True
for line in sys.stdin:
    if line == "OPEN\n":
        if not first:
            pass
            print("")
        amt = {} # name -> amt
        entered = {} # name -> entered
        line = sys.stdin.readline()
        while line != "CLOSE\n":
            dir, name, time = line.split()
            if dir == "ENTER":
                entered[name] = time
            elif dir == "EXIT":
                if name in amt:
                    amt[name] += 0.1 * (int(time) - int(entered[name]))
                else:
                    amt[name] = 0.1 * (int(time) - int(entered[name]))
                del entered[name]
            line = sys.stdin.readline()
        names = []
        for n in amt:
            names.append((n, amt[n]))
        names.sort()
        print("Day " + str(day))
        for n in names:
            print(str(n[0]) + " " + "${:0.2f}".format(float(n[1])))
        first = False
        day += 1
