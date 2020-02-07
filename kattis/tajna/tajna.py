import sys
import math

word = sys.stdin.readline().split('\n')[0]
N = len(word)
R, C = 1, N
for i in range(2, int(math.sqrt(N))+1):
    if N % i == 0:
        R, C = i, N // i

arr = []
for i in range(0, R):
    for j in range(0, C):
        arr.append(word[j*R+i])
print(''.join(arr))
