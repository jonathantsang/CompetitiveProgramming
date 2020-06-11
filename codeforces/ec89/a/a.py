n = int(input())

rr = lambda: input()
rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

def solve(a,b):
	amt = 0
	if b > a:
		a,b = b,a
	diff = a-b
	amt += diff

	# attempt to do diff from a side
	if b < diff:
		return b
	else:
		a-=diff*2
		b-=diff
		# do pairs of 3 now
		both = min(a // 3, b // 3)
		amt += both*2

		a -= both*3
		b -= both*3

		# rest as a
		resta = min(a//2, b)

		# rest as b
		restb = min(b//2, a)

	return amt + max(resta,restb)

for _ in range(n):
	a,b = rrm()
	print(solve(a,b))
