import sys

H = sys.stdin.readline().split('\n')[0].split()
if len(H) == 1:
    print(pow(2, int(H[0])+1)-1)
    exit(0)
else:
    path = H[1]
    H = H[0]
H = int(H)

# 1, 2, 3, 4
# 1, 3, 7, 15
# 2^0-1, 2^1-1

maximum = pow(2, H+1)
pos = 1
for p in path:
    pos *= 2
    if p == 'R':
        pos += 1
print(str(maximum - pos))
