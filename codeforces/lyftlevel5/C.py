import sys

n = int(sys.stdin.readline())

line = map(int , sys.stdin.readline().split())



for val in line:
  arr = [0 for i in range(0, n)]
  placed = val-1
  arr[placed] = 1
  ## Can only move
