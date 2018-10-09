#! /usr/bin/python3

import sys

n = sys.stdin.readline()
count = 0
for line in sys.stdin:
	arr = line.split(" ")
	for val in arr:
		if(int(val) < 0):
			count+=1

print(count)