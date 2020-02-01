import sys

n = sys.stdin.readline()

for line in sys.stdin:
    rooms = list(map(int, line.split()))
    ordered = []
    for i, room in enumerate(rooms):
        ordered.append((room, i+1))
    ordered.sort()

    largest = max([val[0] for val in ordered])
    others = sum([val[0] for val in ordered]) - largest
    if largest > others:
        print("impossible")
        break
    else:
        ans = ""
        order = [str(idx[1]) for idx in reversed(ordered)]
        ans = " ".join(order)
        print(ans)
