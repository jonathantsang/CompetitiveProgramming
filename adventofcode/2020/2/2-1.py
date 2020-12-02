import sys
from collections import Counter

valid = 0
for line in sys.stdin:
	bounds,char,passw=line.split()
	char = char.split(':')[0]
	low,high=bounds.split('-')
	low=int(low)
	high=int(high)
	low-=1
	high-=1
	if passw[low]==char and passw[high]!=char or passw[low]!=char and passw[high]==char:
		valid+=1

print(valid)