rr = lambda: input()
rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

INF=float('inf')

def solve(N,K,B):
	B=sorted(B)
	aread = 0
	atotal = 0
	soloa = []
	bread = 0
	btotal = 0
	solob = []
	totaltime = 0

	for time, alike, blike in B:
		#print(time,alike,blike)
		#print(soloa, solob)
		#print(" ")
		if not alike and not blike:
			continue
		if alike and not blike:
			if aread >= K:
				continue # dont add if exclusive and full
			else:
				aread+=1
				soloa.append(time)
				atotal += time
		elif blike and not alike:
			if bread >= K:
				continue # dont add if exclusive and full
			else:
				bread+=1
				solob.append(time)
				btotal += time
		else:
			# check if want to add
			lose = 0
			if aread >= K and len(soloa) > 0:
				lose += soloa[-1]
			if bread >= K and len(solob) > 0:
				lose += solob[-1]

			#print(lose, time)
			# cheaper to read this book, then two separate
			if lose > time or aread < K or bread < K:
				aread += 1
				bread += 1
				totaltime += time

				if aread >= K+1 and len(soloa) > 0:
					atotal -= soloa.pop()
					aread -= 1
				if bread >= K+1 and len(solob) > 0:
					btotal -= solob.pop()
					bread -= 1

	#print(soloa, solob)
	if aread < K or bread < K:
		return -1
	return totaltime + atotal + btotal

n,k = rrm()
books = [] # tuples (time, alice likes it, bob likes it)
for _ in range(n):
	time,a,b=rrm()
	books.append((time,a,b))
print(solve(n,k,books))
