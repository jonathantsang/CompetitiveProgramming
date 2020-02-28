import sys

n = int(input())
c = 1
for line in sys.stdin.readlines():
    want, old, new = list(line.split())
    old_base = len(old)
    col = 1
    num = 0
    for i in range(len(want)-1, -1, -1):
        num += old.index(want[i]) * col
        col *= old_base

    new_base = len(new)
    ans = []
    while num > 0:
        ans.append(new[num % new_base])
        num //= new_base
    print("Case #" + str(c) + ": "+ "".join(reversed(ans)))
    c += 1
