t = int(input())

# int(input())
# list(map(int, input().split()))

def solve(n, arr):
	arr.sort()
	best = float('inf')
	for i in range(1, len(arr)):
		best = min(best, arr[i] - arr[i-1])
	return best

for _ in range(t):
	n = int(input())
	arr = list(map(int, input().split()))

	print(solve(n, arr))
