n = int(input())

def solve(arr):
	total = 0
	sign = -1 if arr[0] < 0 else 1
	prevbest = arr[0]
	for i in range(1, len(arr)):
		#print(i, prevbest)
		if (sign < 0 and arr[i] > 0) or (sign > 0 and arr[i] < 0):
			sign = -1 if sign == 1 else 1
			total += prevbest
			prevbest = arr[i]
		else:
			prevbest = max(prevbest, arr[i])
	total += prevbest
	return total

for _ in range(n):
	leng = int(input())
	arr = list(map(int, input().split()))
	print(solve(arr))
