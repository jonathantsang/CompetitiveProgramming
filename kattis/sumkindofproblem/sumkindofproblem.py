#! /usr/bin/python3
import sys

p = sys.stdin.readline()
lines = sys.stdin.readlines()
for line in lines:
  vals = line.split()
  data_set = vals[0]
  n = int(vals[1])
  total = int(n * (n+1) / 2)
  even = total * 2
  odd = n * n
  print(data_set + ' ' + str(total) + ' ' + str(odd) + ' ' + str(even))