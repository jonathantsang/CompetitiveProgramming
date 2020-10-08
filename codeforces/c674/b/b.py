# from collections import defaultdict

import io, os, math
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

rr = lambda: input()
rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

INF=float('inf')

def solve(N,M,tiles):
	if M%2==1:
		return False
	
	# want MxM grid

	for tile in tiles:
		# check if symmetric
		if tile[1]==tile[2]:
			return True
	#print(seen)
	return False

t = rri()
for _ in range(t):
	N,M=rrm()
	tiles = []
	for _ in range(N):
		top = rrm()
		bottom = rrm()
		top.extend(bottom)
		tiles.append(top)
	if solve(N,M,tiles):
		print("YES")
	else:
		print("NO")