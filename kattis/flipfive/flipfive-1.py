import collections

n = int(input())

def flip(grid, i):
    if i == 0:
        grid ^= 1 << 0
        grid ^= 1 << 1
        grid ^= 1 << 3
    elif i == 1:
        grid ^= 1 << 0
        grid ^= 1 << 1
        grid ^= 1 << 2
        grid ^= 1 << 4
    elif i == 2:
        grid ^= 1 << 1
        grid ^= 1 << 2
        grid ^= 1 << 5
    elif i == 3:
        grid ^= 1 << 0
        grid ^= 1 << 3
        grid ^= 1 << 4
        grid ^= 1 << 6
    elif i == 4:
        grid ^= 1 << 1
        grid ^= 1 << 3
        grid ^= 1 << 4
        grid ^= 1 << 5
        grid ^= 1 << 7
    elif i == 5:
        grid ^= 1 << 2
        grid ^= 1 << 4
        grid ^= 1 << 5
        grid ^= 1 << 8
    elif i == 6:
        grid ^= 1 << 3
        grid ^= 1 << 6
        grid ^= 1 << 7
    elif i == 7:
        grid ^= 1 << 4
        grid ^= 1 << 6
        grid ^= 1 << 7
        grid ^= 1 << 8
    elif i == 8:
        grid ^= 1 << 5
        grid ^= 1 << 7
        grid ^= 1 << 8
    return grid

for _ in range(0, n):
    grid = 0
    for i in range(0, 3):
        row = input().strip()
        for c in range(0, 3):
            if row[c] == "*":
                grid |= (1 << (i * 3 + c))
    if grid == 0:
        print(0)
        continue

    queue = collections.deque()
    # grid and cost in tuple
    queue.appendleft((grid, 0))

    seen = set()
    found = False
    while len(queue) > 0:
        val = queue.popleft()
        # print(bin(val[0]), val[1])

        if val[0] in seen:
            continue
        seen.add(val[0])

        new_grid = 0
        for i in range(0, 9):
            new_grid = flip(val[0], i)

            if new_grid == 0:
                found = True
                print(val[1]+1)
                break

            if new_grid not in seen:
                queue.append((new_grid, val[1]+1))

        if found:
            break
