import sys

N, K = list(map(int, sys.stdin.readline().split()))
booths = list(map(int, sys.stdin.readline().split()))
booths.sort()

ans = float('inf')
# first number perform for booths[0]
pos = 0
neg = 0
total = 0
for j in range(0, len(booths)):
	want = booths[0] + j * K
	total += abs(want - booths[j])
	if want - booths[j] < 0:
		neg += (want - booths[j])
	else:
		pos += (want - booths[j])
print("total " + str(total))

for j in range(1, len(booths)):
	diff = (booths[j] - booths[0]) - 1
	print("diff " + str(diff))
	
	# diff > 0 always
	replaces = min(abs(neg) // diff, len(booths))
	print("replaces " + str(replaces))
	val = abs(neg + (replaces * diff)) + (len(booths) - replaces) * diff + pos
	print("total " + str(total))

	ans = min(val, ans)
	#adj = total + (diff * len(booths))
	#print(adj)
	#ans = min(adj, ans)
print(ans)

# O(n^2) TLE
# ans = float('inf')
# for i, n in enumerate(booths):
# 	# n is fixed
# 	total = 0
# 	for j in range(0, len(booths)):
# 		want = n + (j - i) * K
# 		total += abs(want - booths[j])
# 	## print("total " + str(total))
# 	ans = min(total, ans)
# print(ans)