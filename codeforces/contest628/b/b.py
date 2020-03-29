t = int(input())
for _ in range(t):
	l = int(input())
	vals = list(map(int, input().split()))
	unique = set()
	for v in vals:
		unique.add(v)
	print(len(unique))