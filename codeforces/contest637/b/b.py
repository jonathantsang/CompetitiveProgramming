import collections

t = int(input())

def solve(arr, k):
	peaks = []
	for i in range(1, len(arr)-1):
		if arr[i-1] < arr[i] > arr[i+1]:
			peaks.append(1)
		else:
			peaks.append(0)
	#print(peaks)

	best = (0, 1) # total p, earliest

	window = collections.deque()
	ones = collections.deque()
	bound = [1, 1]
	for i in range(0, len(peaks)):
		#print(bound[0], window, ones)
		if len(window) < k-2:
			window.append(peaks[i])
			bound[1] += 1
		else:
			# pop the earliest one
			v = window.popleft()
			if v == 1:
				ones.popleft()
			window.append(peaks[i])
			bound[0] += 1
			bound[1] += 1

		if peaks[i] == 1:
			ones.append(peaks[i])

		# check segment
		if len(ones) > best[0] and len(window) == k-2:
			best = (len(ones), bound[0]) # totalp, earliest

	print(best[0]+1, best[1]) # p+1, earliest peak

for _ in range(t):
	n, k = list(map(int, input().split()))
	arr = list(map(int, input().split()))
	solve(arr, k)