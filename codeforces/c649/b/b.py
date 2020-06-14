# from collections import deque

t = int(input())

INF=float('inf')

rr = lambda: input()
rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

def solve(N, arr):
	ans = [arr[0]]
	dir = None # increasing or decreasing
	i = 1
	while i < N:
		if dir == None and arr[i] != ans[0]:
			if arr[i] < ans[0]:
				dir = 'dec'
			else:
				dir = 'inc'
		if dir == 'inc':
			if arr[i] >= arr[i-1]:
				pass
			else:
				dir = 'dec'
				ans.append(arr[i-1])
		else:
			if arr[i] <= arr[i-1]:
				pass
			else:
				dir = 'inc'
				ans.append(arr[i-1])
		i+=1
	if ans[-1] != arr[-1]:
		ans.append(arr[-1])
	print(len(ans))
	print(" ".join(list(map(str, ans))))



for _ in range(t):
	n=rri()
	arr=rrm()
	solve(n,arr)
