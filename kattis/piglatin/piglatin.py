import sys

saved = {}
for line in sys.stdin:
    words = line.split()
    vals = []
    for word in words:
        if word in saved:
            vals.append(saved[word])
            continue
        first = word[0]
        if first in ['a', 'e', 'i', 'o', 'u', 'y']:
            saved[word] = word + "yay"
            vals.append(saved[word])
        else:
            # find first vowel
            for i in range(0, len(word)):
                if word[i] in ['a', 'e', 'i', 'o', 'u', 'y']:
                    saved[word] = word[i:] + word[:i] + "ay"
                    vals.append(saved[word])
                    break
    print(" ".join(vals))
