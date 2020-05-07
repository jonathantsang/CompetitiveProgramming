def checkDifferent(n):
	seen = set()
	for d in str(n):
		if d in seen:
			return False
		seen.add(d)
	return True

def findPrimes(n):
	prime = [True for i in range(n + 1)]
	best = 2
	p = 2
	while (p * p <= n):
		if (prime[p] == True):
			for i in range(p * 2, n + 1, p):
				prime[i] = False
		p += 1
	for i in range(len(prime)-1, -1, -1):
		if prime[i] and checkDifferent(i):
			best = i
			break
	return best

class EllysDifferentPrimes:
	def getClosest(self, N):
		best = findPrimes(N)
		return best