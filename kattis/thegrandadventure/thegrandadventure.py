import sys

n = sys.stdin.readline()

for line in sys.stdin:
    adv = line
    bag = [] # stack
    f = False
    for c in adv:
        if c == '.':
            continue
        elif c in ['$', '*', '|']:
            bag.append(c)
        elif len(bag) == 0 and c in ['t', 'j', 'b']:
            f = True
            break
        elif c == 't':
            if bag[-1] == '|':
                bag.pop()
            else:
                f == True
                break
        elif c == 'j':
            if bag[-1] == '*':
                bag.pop()
            else:
                f == True
                break
        elif c == 'b':
            if bag[-1] == '$':
                bag.pop()
            else:
                f == True
                break
    if f or len(bag) > 0:
        print('NO')
    else:
        print("YES")
