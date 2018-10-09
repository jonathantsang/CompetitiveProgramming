#! /usr/bin/python3

import sys
import math

n = sys.stdin.readline()
vals = n.split(" ")
n = vals[0]
w = int(vals[1])
h = int(vals[2])
d = int(math.sqrt(pow(w, 2) + pow(h, 2)))
compare = d

for line in sys.stdin:
	if(int(line) <= compare):
		print("DA")
	else:
		print("NE")