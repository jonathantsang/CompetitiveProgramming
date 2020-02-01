#! /usr/bin/python3

import sys
import math

nm = list(map(int, sys.stdin.readline().split()))

n = nm[0]
m = nm[1]

possible = {} # Combination -> Times
best = [] # sorted
bestsofar = 0

for i in range(1, n+1):
	for j in range(1, m+1):
		if (i + j) in possible:
			possible[i+j] += 1
		else:
			possible[i+j] = 1
# print(possible)
for combo in possible:
	if possible[combo] > bestsofar:
		best = []
		bestsofar = possible[combo]
		best.append(combo)
	elif possible[combo] == bestsofar:
		best.append(combo)
best.sort()
for val in best:
	print(val)

