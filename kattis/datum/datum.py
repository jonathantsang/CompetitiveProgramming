#! /usr/bin/python3

import sys
import math

# 2009
# 1 1 thursday
day = { 0: "Thursday", 1: "Friday", 2: "Saturday", 3: "Sunday", 4: "Monday", 5: "Tuesday", 6: "Wednesday"}
dm = list(map(int, sys.stdin.readline().split()))
d = dm[0]
m = dm[1]
total_d = d-1

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for i in range(0, m-1):
	total_d += months[i]

print(day[total_d % 7])