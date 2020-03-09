n = int(input())
h, w = 8, 8
seq = []

def traverse(x1, y1, x2, y2, moves, seen):
    global seq
    if (x1, y1) in seen and seen[(x1, y1)] <= len(moves):
        return
    seen[(x1, y1)] = len(moves)
    if x1 == x2 and y1 == y2 and len(moves) < 4:
        # print("found")
        if seq == []:
            seq = moves.copy()
        return
    if len(moves) == 4:
        return
    a = x1-1
    b = y1-1
    # nw diag
    while a >= 0 and b >= 0:
        moves.append((a, b))
        traverse(a, b, x2, y2, moves, seen)
        moves.pop(-1)
        a -= 1
        b -= 1
    a = x1-1
    b = y1+1
    # sw diag
    while a >= 0 and b < h:
        moves.append((a, b))
        traverse(a, b, x2, y2, moves, seen)
        moves.pop(-1)
        a -= 1
        b += 1
    a = x1+1
    b = y1-1
    # ne diag
    while a < w and b >= 0:
        moves.append((a, b))
        traverse(a, b, x2, y2, moves, seen)
        moves.pop(-1)
        a += 1
        b -= 1
    a = x1+1
    b = y1+1
    # nw diag
    while a < w and b < h:
        moves.append((a, b))
        traverse(a, b, x2, y2, moves, seen)
        moves.pop(-1)
        a += 1
        b += 1

for _ in range(0, n):
    x1, y1, x2, y2 = input().split()
    y1, y2 = h-int(y1), h-int(y2)
    x1 = ord(x1) - ord('A')
    x2 = ord(x2) - ord('A')
    seq = []

    # even-even and odd-odd reach
    # even-odd and odd-even reach
    if (x1 % 2 == y1 % 2) and (x2 % 2 != y2 % 2):
        print("Impossible")
        continue
    elif (x1 % 2 != y1 % 2) and (x2 % 2 == y2 % 2):
        print("Impossible")
        continue
    # should be possible and bishop should be able to get to any square in < 3 moves
    traverse(x1, y1, x2, y2, [], {})
    ans = []
    ans.append(str(len(seq)))
    ans.append(chr(x1 + ord('A')))
    ans.append(str(8 - y1))
    for v in seq:
        ans.append(chr(v[0] + ord('A')))
        ans.append(str(8-v[1]))
    # ans.append(chr(x2 + ord('A')))
    # ans.append(str(8 - y2))
    print(" ".join(ans))
