# from collections import defaultdict

rr = lambda: input()
rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

INF=float('inf')

def solve(x,y,z):
	# x = max(a,b)
	# y = max(a,c)
	# z = max(b,c)
	vals = [x,y,z]

	for i in range(3): # rotate x,y,z
		x = vals[i % 3]
		y = vals[(i+1) % 3]
		z = vals[(i+2) % 3]
		
		# y > x, x > z
		# try a = x, c = y, b = a
		a = x
		c = y
		b = a
		if x == max(a,b) and y == max(a,c) and z == max(b,c):
			print("YES")
			print(a, b, c)
			return

	print("NO")



n = rri()
for _ in range(n):
	x,y,z=rrm()
	solve(x,y,z)
