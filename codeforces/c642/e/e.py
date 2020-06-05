t = int(input())

def solve(N, K, A):
    P = [0]
    for x in A: P.append(P[-1] + x)
    for _ in range(K + 1): P.append(P[-1])
    
    ans = sum(A)
    if ans > 0:
        ans -= 1
    # handled 0 and 1 light on already
    INF = float('inf')
    dp = [INF] * (N + 1)
    # dp[i] : cost of garland starting here
    for i in range(N-1, -1, -1):
        # 1 + 000000 + 1*
        # A[i] must be 1
        # base cost: make 1000000
        #      = cost + zerocost for A[i+1...]
        cost = A[i] ^ 1
        dp[i] = basecost = cost + P[-1] - P[i+1]
 
        # or, we could make 1, some zeros, then dp[i + K]
        if i + K < N:
            cand = cost + P[i+K] - P[i+1] + dp[i+K]
            if cand < basecost:
                dp[i] = cand
    s = 0
    for i, x in enumerate(A):
        dp[i] += s
        s += x
    
    ans2 = min(dp)
    if ans2 < ans:
        ans = ans2
    return ans

for _ in range(t):
	n, k = list(map(int, input().split()))
	s = list(map(int, list(input())))
	print(solve(n, k, s))

# inc