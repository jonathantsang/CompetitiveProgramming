import sys
from collections import Counter

valid = 0
for line in sys.stdin:
	bounds,char,passw=line.split()
	char = char.split(':')[0]
	low,high=bounds.split('-')
	c = Counter(passw)
	if int(low)<=c[char]<=int(high):
		valid += 1

print(valid)