import sys

rc = sys.stdin.readline().split()
r = int(rc[0])
c = int(rc[1])
ors = []

possible = []
mat = []
# Each value in the matrix
for i in range(0, r):
  row = list(map(int, sys.stdin.readline().split()))
  mat.append(row)
  
s = {}
for j in range(0, len(mat[0])):
  if mat[0][j] not in s:
    # array with: indicies in columns at each row, or so far
    possible.append([[j], mat[0][j]])
    s[mat[0][j]] = 1

  
# Each column
for i in range(1, r):
  row = []
  # Each value in the matrix row  
  for j in range(0, c):
    seen = {}
    if mat[i][j] in seen:
      continue
    else:
      seen[mat[i][j]] = 1
    # Each value in the possible
    for k in range(0, len(possible)):
      # mat[i][j]
      val = possible[0].copy()
      val[0] = possible[0][0].copy()
      val[0].append(j)
      val[1] ^= mat[i][j]
      row.append(val)
  possible = row

found = False
for l in possible:
  if l[1] > 0:
    print("TAK")
    found = True
    ans = ""
    for i in range(0, len(l[0])):
      if i != 0:
        ans += ' '
      ans += str(l[0][i]+1)
    print(ans)
    break

if found == False:
  print("NIE")
