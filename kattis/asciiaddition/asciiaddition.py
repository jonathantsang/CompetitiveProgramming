import sys

def checkNum(grid, i):
    # +
    if grid[0][i:i+5] == ".....":
        return "+"
    # 1
    elif grid[0][i:i+5] == "....x":
        return 1
    # 4
    elif grid[0][i:i+5] == "x...x":
        return 4
    else:
        if grid[1][i:i+5] == "....x":
            # 2
            if grid[4][i:i+5] == "x....":
                return 2
            # 3
            else:
                if grid[3][i:i+5] == "xxxxx":
                    return 3
                return 7
        elif grid[1][i:i+5] == "x....":
            # 5
            if grid[4][i:i+5] == "....x":
                return 5
            # 6
            else:
                return 6
        else:
            # 8
            if grid[4][i:i+5] == "x...x":
                if grid[3][i:i+5] == "x...x":
                    return 0
                return 8
            # 9
            else:
                return 9

exp = []
for _ in range(0, 7):
    exp.append(sys.stdin.readline().split('\n')[0])

vals = []
for i in range(0, len(exp[0]) // 6+1):
    vals.append(str(checkNum(exp, i*6)))

vals = "".join(vals)
vals = vals.split('+')
ans = int(vals[0])+int(vals[1])

toprint = [[] for _ in range(0, 7)]
for c in str(ans):
    loader = ["" for _ in range(0, 7)]
    if c == '1':
        for i in range(0, 7):
            loader[i] = "....x"
    elif c == '2':
        loader[0] = "xxxxx"
        loader[1] = "....x"
        loader[2] = "....x"
        loader[3] = "xxxxx"
        loader[4] = "x...."
        loader[5] = "x...."
        loader[6] = "xxxxx"
    elif c == '3':
        loader[0] = "xxxxx"
        loader[1] = "....x"
        loader[2] = "....x"
        loader[3] = "xxxxx"
        loader[4] = "....x"
        loader[5] = "....x"
        loader[6] = "xxxxx"
    elif c == '4':
        loader[0] = "x...x"
        loader[1] = "x...x"
        loader[2] = "x...x"
        loader[3] = "xxxxx"
        loader[4] = "....x"
        loader[5] = "....x"
        loader[6] = "....x"
    elif c == '5':
        loader[0] = "xxxxx"
        loader[1] = "x...."
        loader[2] = "x...."
        loader[3] = "xxxxx"
        loader[4] = "....x"
        loader[5] = "....x"
        loader[6] = "xxxxx"
    elif c == '6':
        loader[0] = "xxxxx"
        loader[1] = "x...."
        loader[2] = "x...."
        loader[3] = "xxxxx"
        loader[4] = "x...x"
        loader[5] = "x...x"
        loader[6] = "xxxxx"
    elif c == '7':
        loader[0] = "xxxxx"
        loader[1] = "....x"
        loader[2] = "....x"
        loader[3] = "....x"
        loader[4] = "....x"
        loader[5] = "....x"
        loader[6] = "....x"
    elif c == '8':
        loader[0] = "xxxxx"
        loader[1] = "x...x"
        loader[2] = "x...x"
        loader[3] = "xxxxx"
        loader[4] = "x...x"
        loader[5] = "x...x"
        loader[6] = "xxxxx"
    elif c == '9':
        loader[0] = "xxxxx"
        loader[1] = "x...x"
        loader[2] = "x...x"
        loader[3] = "xxxxx"
        loader[4] = "....x"
        loader[5] = "....x"
        loader[6] = "xxxxx"
    elif c == '0':
        loader[0] = "xxxxx"
        loader[1] = "x...x"
        loader[2] = "x...x"
        loader[3] = "x...x"
        loader[4] = "x...x"
        loader[5] = "x...x"
        loader[6] = "xxxxx"
    for i in range(0, len(loader)):
        toprint[i].append(loader[i])

for r in toprint:
    print('.'.join(r))
