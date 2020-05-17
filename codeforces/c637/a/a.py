n = int(input())

for _ in range(n):
	n, a, b, c, d = list(map(int, input().split()))
	each = [a-b, a+b]
	package = [c-d, c+d]
	possible = [each[0]*n, each[1]*n]
	#print(each)
	#print(package)
	#print(possible)
	# check if package and possible overlap
	fine = False
	if package[1] >= possible[0] and package[1] <= possible[1]:
		fine = True
	elif possible[1] >= package[0] and possible[1] <= package[1]:
		fine = True

	if fine:
		print("Yes")
	else:
		print("No")