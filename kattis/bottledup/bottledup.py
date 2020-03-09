amt, b1, b2 = list(map(int, input().split()))
dp = [(float('inf'),float('inf')) for i in range(0, amt+1)]
dp[0] = (0, 0) # b1 and b2 bottles used
for i in range(1, amt+1):
    if i >= b1:
        if sum(dp[i-b1])+1 < sum(dp[i]):
            dp[i] = (dp[i-b1][0]+1,dp[i-b1][1])
    if i >= b2:
        if sum(dp[i-b2])+1 < sum(dp[i]):
            dp[i] = (dp[i-b2][0],dp[i-b2][1]+1)
if dp[i][0] != float('inf'):
    print("{0} {1}".format(dp[amt][0], dp[amt][1]))
else:
    print("Impossible")
