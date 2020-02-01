
n = int(input())

for i in range(n):
	cities = int(input())
	ht = {}
	for j in range(cities):
		name = input()
		if name.islower() and len(name) >= 1 and not (" " in name):
			if name not in ht:
				ht[name] = 1
	print(len(ht))
