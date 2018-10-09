#! /usr/bin/python3

import sys

arr = []
for line in sys.stdin:
	vals = line.split(" ")
	arr = list(map(lambda x: int(x), vals))
	arr.sort()
	diff1 = arr[1]-arr[0];
	diff2 = arr[2]-arr[1];
	if(diff1 == diff2):
		print(arr[2]+diff1)
	else:
		if(diff1 < diff2):
			print(arr[1]+diff1)
		else:
			print(arr[0]+diff2)