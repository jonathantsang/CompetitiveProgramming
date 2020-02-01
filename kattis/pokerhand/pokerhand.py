#! /usr/bin/python3

import sys
import math

hand = sys.stdin.readline().split()
ranks = {}
for card in hand:
	rank = card[0]
	if rank in ranks:
		ranks[rank] += 1
	else:
		ranks[rank] = 1

best = 1
for rank in ranks:
	best = max(ranks[rank], best)
print(best)
