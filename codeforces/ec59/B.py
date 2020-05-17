#! /usr/bin/python3

import sys
import math

store = {} # key is digital root, value: is the ith value
last = 0

def digitalroot(num):
  orig = int(num)
  num = str(num)
  while(len(num) > 1):
    total = 0
    for digit in num:
      total += int(digit)
    num = str(total)
    
  if int(num) in store:
    store[int(num)].append(orig)
  else:
    store[int(num)] = [orig]

def find(k, x):
  global last
  iteration = 1
  i = last
  while True:
    if x in store and len(store[x]) >= k+1:
      last = i
      return store[x][k-1]
    else:
      digitalroot(i)
    i += 1
    
n = int(sys.stdin.readline())
for i in range(0, n):
  kx = list(map(int, sys.stdin.readline().split()))
  k = int(kx[0])
  x = int(kx[1])
  val = find(k, x)
  print(val)