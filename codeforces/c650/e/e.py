from collections import Counter

rr = lambda: input()
rri = lambda: int(input())
rrm = lambda: list(map(int, input().split()))

INF=float('inf')

def solve(N, K, S):
    count = [0] * 26
    for c in S:
        ci = ord(c) - ord('a')
        count[ci] += 1
    count.sort(reverse=True)
    while count and count[-1] == 0:
        count.pop()
    # one bead necklace
    #print("!", count)
    ans = 0  #count[0]
    for r in range(1, N + 1):
        bns = 0
        for c in count:
            bns += c // r
        # there's r pieces, each piece up to bns beads
        #print("!", r, bns)
        for x in xrange(1, bns + 1):
            tot = x * r
            if K % x == 0:
                if tot > ans:
                    ans = tot
                    #print("flag", tot)

    #print("answering", S, ans)
    return ans

t = int(input())
for _ in range(t):
	n,k=rrm()
	s=list(input())
	print(solve(n,k,s))

# from awice
