#! /usr/bin/python3

import sys
import math

while True:
	n = int(sys.stdin.readline())
	if n == -1:
		break
	timesofar = 0
	dist = 0
	for i in range(0, n):	
		st = list(map(int, sys.stdin.readline().split()))
		s = st[0]
		t = st[1]
		
		dist += (t - timesofar) * s
		timesofar = t
	print(str(dist) + " miles")

