#! /usr/bin/python3

import sys
import math

f = [1, 0]
g = [0, 1]

for i in range(2, 31):
	f.append(f[i-2] + 2*g[i-1])
	g.append(f[i-1] + g[i-2])

for line in sys.stdin:
	l = int(line)
	if l == -1:
		break
	if l % 2 == 1:
		print(0)
	else:
		if l == 0:
			print(f[0])
		elif l == 1:
			print(f[1])
		else:
			print(f[l])


