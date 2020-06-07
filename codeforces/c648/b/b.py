t = int(input())
for qwe in range(t):
	n = int(input())
	a = list(map(int, input().split()))
	b = list(map(int, input().split()))
	if (min(b) != max(b)):
		print("Yes")
	else:
		if list(sorted(a)) == a:
			print("Yes")
		else:
			print("No")

# By veschii_nevstrui
