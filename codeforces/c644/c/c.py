t = int(input())

# int(input())
# list(map(int, input().split()))

def solve(n, arr):
	arr.sort()
	odd = 0
	even = 0
	both = 0
	i = 0
	while i < len(arr):
		if i < len(arr)-1 and arr[i] + 1 == arr[i+1]:
			both += 1
			i += 2
			continue
		else:
			if arr[i] & 1 == 1:
				odd += 1
			else:
				even += 1
			i += 1
	if (even & 1 == 0 and odd & 1 == 0):
		return "YES"
	elif (even & 1 == 1 and odd & 1 == 1 and both >= 1):
		return "YES"
	else:
		return "NO"

for _ in range(t):
	n = int(input())
	arr = list(map(int, input().split()))
	print(solve(n, arr))
