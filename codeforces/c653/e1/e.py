from collections import defaultdict, deque

rr = lambda: input()
rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

INF=float('inf')

def solve(N,K,B):
	groups = defaultdict(list) # alice, bob, both books
	for time,alike,blike in B:
		if alike and blike:
			groups['c'].append(time)
		elif alike:
			groups['a'].append(time)
		elif blike:
			groups['b'].append(time)

	for g in groups:
		groups[g] = sorted(groups[g], reverse=True)
	a,b= 0,0
	amt = 0

	while groups['a'] or groups['b'] or groups['c']:
		if not groups['a'] or not groups['b']:
			if not groups['c']:
				break
			amt += groups['c'].pop()
			a+=1
			b+=1
		elif not groups['c'] or groups['a'][-1] + groups['b'][-1] < groups['c'][-1]:
			amt += groups['a'].pop()
			amt += groups['b'].pop()
			a+=1
			b+=1
		else:
			amt += groups['c'].pop()
			a+=1
			b+=1
		if a == K and b == K:
			break
	if a < K or b < K:
		return -1
	return amt

n,k = rrm()
books = [] # tuples (time, alice likes it, bob likes it)
for _ in range(n):
	time,a,b=rrm()
	books.append((time,a,b))
print(solve(n,k,books))
