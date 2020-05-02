n = int(input())

for _ in range(n):
	leng = int(input())
	if leng % 2 == 0 and (leng // 2) % 2 != 0:
		print("NO")
		continue
	else:
		print("YES")
		ans = []
		# even first
		for i in range(1, leng+1):
			if i % 2 == 0:
				ans.append(str(i))
		# odd
		for i in range(leng+1, 0, -1):
			if i % 2 != 0 and i != leng // 2 + 1: # not mid or even
				ans.append(str(i))
		print(" ".join(ans))
