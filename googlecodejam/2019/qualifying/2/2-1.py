import sys

n = int(sys.stdin.readline())
for t in range(1, n+1):
	dimension = int(sys.stdin.readline().split('\n')[0])
	lydia = sys.stdin.readline().split('\n')[0] ## Get rid of newline
	path = ""
	xl = 0
	yl = 0
	for c in lydia:
		if c == 'S':
			path += 'E'
		else:
			path += 'S'
	print("Case #" + str(t) + ": " + path)
