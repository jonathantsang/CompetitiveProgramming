import collections

t = int(input())

def solve(s):
	# try period 1
	p1 = True
	same = s[-1]
	for i in range(len(s)-2, -1, -1):
		if s[i] != same:
			p1 = False
			break
	if p1:
		print(s)
		return
	# try period n
	period = len(s) - i
	block = i + 1
	#print(s)
	print(period)
	if period >= 3:
		while ((len(s) - period) * period) + period > 2 * len(s):
			period += 1
	print(period)

	ans = collections.deque()
	for i in range(period):
		ans.appendleft(s[len(s)-i-1])

	for i in range(len(s)-period-1, -1, -1):
		#print(ans)
		while s[i] != ans[period-1]:
			ans.appendleft(ans[period-1])
		ans.appendleft(s[i])
		#print(ans)
	print("".join(ans))

for _ in range(t):
	s = input()
	solve(s)