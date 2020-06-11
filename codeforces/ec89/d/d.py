import math

rr = lambda: input()
rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

def check(n):
	for i in range(2, int(math.sqrt(n))+1):
		if n % i == 0 and math.gcd(i + n//i,n) == 1:
			return i, n//i
	return -1,-1

def solve(n, arr):
	d2 = []
	d1 = []
	for v in arr:
		a,b = check(v)
		d1.append(a)
		d2.append(b)
	print(' '.join(list(map(str, d1))))
	print(' '.join(list(map(str, d2))))

n = rri()
arr=rrm()
solve(n, arr)
