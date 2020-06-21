from collections import Counter

rr = lambda: input()
rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

INF=float('inf')

def verify(s, arr):
	amts = []
	for i in range(0, len(s)):
		amt = 0
		for j in range(0, len(s)):
			if s[i] < s[j]:
				amt += abs(i-j)
		amts.append(amt)
	print(arr, amts)
	return all(arr[i] == amts[i] for _ in range(len(arr)))

def solve(S,M,arr):
	count = Counter(S)
	chars = [c for c in count]
	chars.sort()
	chars.reverse() # largest first
	ans = ['a' for _ in range(len(arr))]
	valid = True
	i = 0
	while valid:
		#print(arr)
		indices = []
		for j in range(0, len(arr)):
			if arr[j] == 0:
				indices.append(j)
		if indices == []:
			break
		#print(chars, count, indices)
		while i < len(chars) and count[chars[i]] < len(indices):
			i+=1
		for ind in indices:
			arr[ind] = INF
			ans[ind] = chars[i]
		#print(ans)

		# update b val
		for j in range(0, len(arr)):
			if arr[j] != INF:
				for ind in indices:
					arr[j] -= abs(j-ind)

		valid = False
		for v in arr:
			if v != INF:
				valid = True
		i += 1

	return "".join(ans)


q = int(input())
for _ in range(q):
	s=input()
	m=rri()
	arr=rrm() # of length m
	print(solve(s,m,arr))
