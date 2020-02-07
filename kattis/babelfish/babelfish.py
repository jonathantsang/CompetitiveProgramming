import sys

mode = "read"
words = {}
for line in sys.stdin:
    if mode == "read":
        try:
            old, foreign = line.split()
            words[foreign] = old
        except ValueError:
            mode = "print"
    elif mode == "print":
        word = line.split()[0]
        if word in words:
            print(words[word])
        else:
            print("eh")
