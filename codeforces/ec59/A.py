#! /usr/bin/python3

import sys
import math

n = int(sys.stdin.readline())

for i in range(0, n):
  leng = int(sys.stdin.readline().split('\n')[0])
  query = str(sys.stdin.readline().split('\n')[0])
  if leng > 2:
    print("YES")
    print("2")
    print(query[:1] + ' ' + query[1:])
  elif leng == 2:
    if query[0] >= query[1]:
      print("NO")
    else:
      print("YES")
      print("2")
      print(query[0] + ' ' + query[1])   
  else:
    print("NO")