t = int(input())

# int(input())
# list(map(int, input().split()))

def solve(n):
	val = bin(n)[2:]
	#print(n, val)
	amt = 0
	prev = 0
	for i, b in enumerate(val):
		if b == '1':
			added = prev*2+1
			amt += added
			prev = added
		elif b == '0':
			added = prev*2
			amt += added
			prev = added

	return amt

for _ in range(t):
	n = int(input())
	print(solve(n))
