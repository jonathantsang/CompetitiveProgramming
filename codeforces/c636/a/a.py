n = int(input())

for _ in range(n):
	i  = 2
	s = 3
	num = int(input())
	while not num % s == 0:
		s += 2**i
		i += 1
	print(num // s)
