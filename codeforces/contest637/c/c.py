t = int(input())

def solve(arr):
	valid = True

	increasing = True
	for i in range(0, len(arr)-1):
		if arr[i] < arr[i+1]:
			increasing = False
	if increasing:
		print("Yes")
		return

	i = len(arr)-1
	while i > 0:
		#print("i", i)
		if i > 0 and arr[i] < arr[i-1]:
			j = i-1
			# check sequence strictly increasing +1
			while j > 0 and arr[j] - 1 == arr[j-1]:
				#print("j", j)
				j -= 1
			i = j
		else:
			print("No")
			return
	print("Yes")
	return


for _ in range(t):
	n = int(input())
	arr = list(map(int, input().split()))
	solve(arr)