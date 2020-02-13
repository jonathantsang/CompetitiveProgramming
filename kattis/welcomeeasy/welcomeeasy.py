import sys

amt = 0

def check(idx, loc, line, word):
    global amt
    if loc == len(word):
        amt += 1
        return
    for i in range(idx, len(line)):
        if word[loc] == line[i]:
            check(i+1, loc+1, line, word)

n = int(sys.stdin.readline())
want = "welcome to code jam"

for i in range(0, n):
    line = sys.stdin.readline()
    amt = 0
    check(0, 0, line, want)

    print("Case #{0}: {1}".format(i+1, str(amt).zfill(4)))
