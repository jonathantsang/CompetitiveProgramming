n = int(input())

# Create a boolean array "prime[0..n]" and initialize
# all entries it as true. A value in prime[i] will
# finally be false if i is Not a prime, else true.
primes = [True for i in range(32100 + 1)]
def SieveOfEratosthenes(n):
    p = 2
    while (p * p <= n):
        # If prime[p] is not changed, then it is a prime
        if (primes[p] == True):
            # Update all multiples of p
            for i in range(p * 2, n + 1, p):
                primes[i] = False
        p += 1
    primes[0]= False
    primes[1]= False

SieveOfEratosthenes(32100)

for i in range(0, n):
    num = int(input())
    pairs = []
    for v in range(0, len(primes)):
        if v > num // 2:
            break
        if primes[v] == True and primes[num-v] == True:
            pairs.append((v, num-v))
    print("{0} has {1} representation(s)".format(num, len(pairs)))
    for p in pairs:
        print("{0}+{1}".format(p[0],p[1]))
    if i+1 != n:
        print("")
