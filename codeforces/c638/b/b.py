t = int(input())

def solve(n, k, arr):
	ans = []
	segment = []
	seen = set()
	for v in arr:
		seen.add(v)
	if len(seen) > k:
		print(-1)
		return

	# Fill remaining
	idx = 1
	while idx <= n and len(seen) < k:
		seen.add(idx)
		idx += 1

	# need exact length
	if len(seen) != k:
		print(-1)
		return

	for v in seen:
		segment.append(v)

	for v in arr:
		ans.extend(segment)
	print(len(ans))
	print(" ".join(list(map(str, ans))))


for _ in range(t):
	n, k = list(map(int, input().split()))
	arr = list(map(int, input().split()))
	solve(n, k, arr)