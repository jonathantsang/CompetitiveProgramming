import sys

word = sys.stdin.readline().split('\n')[0]

# ..#..
# .#.#.
# #.A.#
# .#.#.
# ..#..

# ..*..
# .*.*.
# *.X.*
# .*.*.
# ..*..

lines = [[] for _ in range(0, 5)]
for i, c in enumerate(word):
    if i % 3 == 2:
        # wendy
        lines[0].append("..*..")
        lines[1].append(".*.*.")
        lines[2].append("*." + c + ".*")
        lines[3].append(".*.*.")
        lines[4].append("..*..")
    else:
        # peter pan frame
        if i % 3 != 0 or i == 0:
            lines[0].append(".")
            lines[1].append(".")
            lines[2].append("#")
            lines[3].append(".")
            lines[4].append(".")
        lines[0].append(".#.")
        lines[1].append("#.#")
        lines[2].append("." + c + ".")
        lines[3].append("#.#")
        lines[4].append(".#.")
        if i + 1 == len(word):
            lines[0].append(".")
            lines[1].append(".")
            lines[2].append("#")
            lines[3].append(".")
            lines[4].append(".")
for l in lines:
    print("".join(l))
