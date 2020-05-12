#! /usr/bin/python3

import sys
import math

def digitalroot(num):
  orig = int(num)
  num = str(num)
  while(len(num) > 1):
    total = 0
    for digit in num:
      total += int(digit)
    num = str(total)
  return int(num)


for i in range(0, 110):
  arr = []
  for j in range(i*10, i*10+10):
    arr.append(digitalroot(j))
  print(arr)

n = int(sys.stdin.readline())
for i in range(0, n):
  kx = list(map(int, sys.stdin.readline().split()))
  k = int(kx[0])
  x = int(kx[1])

  altered = k - 1
  
  shiftfactor = altered % 10
  
  altered *= 10
  
  print(val)