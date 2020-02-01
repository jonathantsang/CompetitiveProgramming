import sys

N, P = list(map(int, sys.stdin.readline().split()))
each = list(map(int, sys.stdin.readline().split()))

dp = [0 for _ in range(0, len(each))]
for i in range(0, len(each)):
    dp[i] = max(dp[i], dp[i-1]+each[i]-P)
print(max(dp))
