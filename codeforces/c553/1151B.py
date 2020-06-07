import sys

rc = sys.stdin.readline().split()
r = int(rc[0])
c = int(rc[1])
ors = []
ans = []
mat = []
# Each value in the matrix
for i in range(0, r):
  row = list(map(int, sys.stdin.readline().split()))
  mat.append(row)
  
dp = [[]]
s = {}
for j in range(0, len(mat[0])):
  if mat[0][j] not in s:
    # array with: indicies in columns at each row, or so far
    dp[0].append(([j], mat[0][j]))
    s[mat[0][j]] = 1

# Go through matrix rows
for i in range(1, r):
  seen = {}
  row = []
  # Each row element
  for j in range(0, c):
    if mat[i][j] not in s:
      
      # For each possible backwards value
      for k in range(0, len(dp[i-1])):
        
        # Add to next row, regardless of 0
        # if dp[i-1][k][1] ^ mat[i][j] > 1:
        arr = dp[i-1][k][0]
        orsa = dp[i-1][k][1]
        arr.append(j)
        orsa ^= mat[i][j]
        val = (arr, orsa)
        row.append(val)
      
      s[mat[i][j]] = 1
  dp.append(row)
  
for l in dp:
  print(l)

if len(dp[-1]) > 0 and len(dp[-1][0]) > 0 and len(dp[-1][0][0]) == r:
  print('TAK')
  ans = ''
  for i in range(0, len(dp[-1][0][0])):
    if i != 0:
      ans += ' '
    ans += str(dp[-1][0][0][i]+1) ## +1 indicies
  print(ans)
else:
  print('NIE')

