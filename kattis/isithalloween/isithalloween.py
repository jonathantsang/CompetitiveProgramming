#! /usr/bin/python3

import sys
import math

line = sys.stdin.readline()
date = line.split()
if (date[0] == "OCT" and date[1] == "31") or (date[0] == "DEC" and date[1] == "25"):
	print("yup")
else:
	print("nope")

