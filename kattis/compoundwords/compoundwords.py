import sys

words = dict()
finalWords = [] ## sort
parts = []
for line in sys.stdin:
  line = line.split()
  for a in line:
    parts.append(a)

for i in range(0, len(parts)):
  for j in range(0, len(parts)):
    if i == j:
      continue
    string = parts[i] + parts[j]
    if string not in words:
      words[string] = 1

for w in words:
  finalWords.append(w)
finalWords.sort()

for word in finalWords:
  print(word)