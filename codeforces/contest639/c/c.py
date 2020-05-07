t = int(input())

def solve(n, arr):
	rooms = set() # room #
	for i, v in enumerate(arr):
		newroom = i + arr[i % n]
		if newroom in rooms:
			return "NO"
		rooms.add(newroom)
	return "YES"

for _ in range(t):
	n = int(input())
	arr = list(map(int, input().split()))
	print(solve(n, arr))