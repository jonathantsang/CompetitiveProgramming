from collections import defaultdict as ddic, deque, Counter

rr = raw_input
rri = lambda: int(raw_input())
rrm = lambda: map(int, raw_input().split())
MOD = 10**9 + 7

import bisect
def solve(N, A):
    A = A[::-1]
    dp = []
    for x in A:
        i = bisect.bisect_left(dp, x)
        if i >= len(dp):
            dp.append(x)
        dp[i] = x
    return len(dp)
N = rri()
A = rrm()
print solve(N, A)
