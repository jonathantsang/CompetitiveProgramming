from collections import defaultdict

rr = lambda: input()
rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

INF=float('inf')

def solve(N,M,T,visits,tests):
	seen = defaultdict(lambda: -1) # person -> result (1 = true, 0 = false, -1 = unsure)

	for person, res in tests:
		seen[person] = res # set to 1 or 0 on t-day

	#print(seen)

	for time in sorted(list(visits.keys()), reverse=True):
		meetings = visits[time]

		changes = defaultdict(lambda: -1) # person -> new change

		# if person is in contact with +, contracted
		# if person is in contact with -, safe
		# if person is in contact with BOTH

		# race condition on same day
		# + ?
		# - ?
		# ? ? ???

		for A,B in meetings:
			#print(A,B)
			changes[A]=max(changes[A],seen[A],seen[B])
			changes[B]=max(changes[B],seen[B],seen[A])
			#print(changes)

		#print(changes)
		# check changes
		for person in changes:
			seen[person]=changes[person]

	#print(seen)
	for ith in range(1,N+1):
		if ith in seen:
			if seen[ith] == 1:
				print("+")
			elif seen[ith] == 0:
				print("-")
			else:
				print("?")
		else:
			print("?")

N,M,T=rrm()

visits = defaultdict(list) # time -> meetings (A,B)
for _ in range(M):
	D, A, B = rrm()
	visits[D].append((A,B))

tests = []
for _ in range(T):
	resperson = rr()
	res = resperson[0]
	person = int(resperson[1:])
	tests.append((person, 1 if res=='+' else 0)) # (person, true or false)

solve(N,M,T,visits,tests)
