import sys

rows = {} # row -> count
i = 0
rowlen = -1
collen = 0
start = True
first = True

for line in sys.stdin:
    rows[i] = 0
    if line == "\n":
        offset = 0
        for i in range(0, collen):
            # dots + offset + stars = rowlen
            stars = rows[i]
            dots = rowlen - stars - offset

            piece = ""
            for j in range(0, offset):
                piece = "." + piece

            for j in range(0, stars):
                piece = "*" + piece

            for j in range(0, dots):
                piece = "." + piece

            offset += stars
            print(piece)
        rows = {}
        i = 0
        rowlen = -1
        collen = 0
        start = True
        first = False
    else:
        if start and not first:
            print('\n')
            start = False
        rowlen = len(line)-1 # no \n
        for c in line:
            if c == "*":
                rows[i] += 1
        i += 1
        collen += 1

# last one
offset = 0
for i in range(0, collen):
    # dots + offset + stars = rowlen
    stars = rows[i]
    dots = rowlen - stars - offset

    piece = ""
    for j in range(0, offset):
        piece = "." + piece

    for j in range(0, stars):
        piece = "*" + piece

    for j in range(0, dots):
        piece = "." + piece

    offset += stars
    print(piece)
